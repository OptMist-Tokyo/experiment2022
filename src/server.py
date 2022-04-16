import logging,time
from gpiozero import Button
import weather

# TODO: 今度ラズパイを触る時にピンの番号を指定する。
BUTTON_S2T_PIN = 10
BUTTON_WEATHER_PIN = 11

def init_logging():
    """init_logging

    loggingの一般的な設定をする, またserverという名前のloggerを返す。

    Returns:
        logging.Logger: serverという名前のlogger
    """
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)
    return logging.getLogger(name="server")

def main():
    logger = init_logging()

    button_s2t = Button(BUTTON_S2T_PIN)
    button_weather = Button(BUTTON_WEATHER_PIN)

    logger.info("server started")
    while True:
        if button_s2t.when_pressed:
            # TOOD:録音を開始する関数を呼ぶ
            # TODO:voc2txtを使って認識結果を得る
            # TODO:displayで電光掲示板に表示する
            # TODO:slackに通知する
            pass 
        elif button_weather.when_pressed:
            today_weather,tommorow_weather,tmperature = weather.weather()
            logger.info(f"本日の天気 : {today_weather},本日の気温: {tmperature}度,明日の天気: {tommorow_weather}")
            # TODO:displayで電光掲示板に表示する
            # TODO:slackに通知する
        else:
            time.sleep(0.05)

if __name__ == "__main__":
    main()