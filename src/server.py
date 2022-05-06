import logging,time,datetime
from gpiozero import Button

import weather
import slack
import voc2txt
import display
import schedule

BUTTON_S2T_PIN = 6
BUTTON_WEATHER_PIN = 20

CHANNEL_NAME = "test"

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
    message = f"本日の天気 : {today_weather},本日の気温: {tmperature}度,明日の天気: {tommorow_weather}"
    logger.info(message)
    display.display.createPPM([[message,[255,255,0]]])
    slack.slackbot.send_message(f"本日の天気 : {today_weather},本日の気温: {tmperature}度,明日の天気: {tommorow_weather}")

def speech_call():
    logger.info("speech!")
    ret = voc2txt.s2t.s2t()
    if ret[:6] == "error:":
        logger.error(ret)
        slack.slackbot.send_message("認識に失敗しました")
        display.display.createPPM([["認識に失敗しました",[255,255,0]]])
    else:
        slack.slackbot.send_message(ret)
        display.display.createPPM([[ret,[255,255,0]]])

def main():
    button_s2t = Button(BUTTON_S2T_PIN)
    button_weather = Button(BUTTON_WEATHER_PIN)

    logger.info("server started")

    # ボタンを押した時のイベント
    button_s2t.when_pressed = speech_call
    button_weather.when_pressed = weather_call

    channel_id = slack.slackbot.get_channel_id(channel_name=CHANNEL_NAME)
    if channel_id is None:
        logger.error(f"slack channel: {CHANNEL_NAME} not found.")
        exit()
    
    # 10秒ごとにslackのメッセージを読む
    # NOTE: conversation_historyの引数oldestにはstr型を与えることになっている。
    # 小数点以下の桁数をちょうど6桁にしないと、チャンネル内メッセージのtimestampとうまく比較できないっぽい
    ts = str(round(time.time(), 6))
    dt = datetime.datetime.now()

    while True:

        # slackからmessageを取得
        logger.info(f"get message older than: {ts}")
        con_hist = slack.slackbot.get_channel_messages(channel_id=channel_id, oldest=ts)
        new_message_flg = False
        for message in con_hist:
            if "bot_id" not in message:
                logger.info(f"\ttext:{message['text']}, ts:{message['ts']}")
                is_schedule = schedule.check_and_reg(message["text"])
                if not is_schedule:
                    display.display.createPPM([[message,[255,255,0]]])
                new_message_flg = True
        
        if new_message_flg == False:
            logger.info("no new message")
        ts = str(round(time.time(), 6))

        # schedule情報を取得
        logger.info(f"get schedule info older than: {ts}")
        dt_now = datetime.datetime.now()
        sched_info = schedule.timer(dt,dt_now)
        for sched in sched_info:
            slack.slackbot.send_message(sched)
            display.display.createPPM([[sched,[255,255,0]]])
        dt = dt_now

        time.sleep(10)

if __name__ == "__main__":
    main()