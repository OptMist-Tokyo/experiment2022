import logging,time
from gpiozero import Button
from signal import pause

import weather
import slack

BUTTON_S2T_PIN = 6
BUTTON_WEATHER_PIN = 20

def init_logging():
    """init_logging

    loggingの一般的な設定をする, またserverという名前のloggerを返す。

    Returns:
        logging.Logger: serverという名前のlogger
    """
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)
    return logging.getLogger(name="server")

logger = init_logging()

def weather_call():
    logger.info("weather!")
    today_weather,tommorow_weather,tmperature = weather.weather()
    logger.info(f"本日の天気 : {today_weather},本日の気温: {tmperature}度,明日の天気: {tommorow_weather}")
    # TODO:displayで電光掲示板に表示する
    slack.slackbot.send_message(f"本日の天気 : {today_weather},本日の気温: {tmperature}度,明日の天気: {tommorow_weather}")

def speech_call():
    logger.info("speech!")
    # TOOD:録音を開始する関数を呼ぶ
    # TODO:voc2txtを使って認識結果を得る
    # TODO:displayで電光掲示板に表示する
    # TODO:slackに通知する

def main():
    button_s2t = Button(BUTTON_S2T_PIN)
    button_weather = Button(BUTTON_WEATHER_PIN)

    logger.info("server started")
    button_s2t.when_pressed = speech_call
    button_weather.when_pressed = weather_call
    pause()

if __name__ == "__main__":
    main()