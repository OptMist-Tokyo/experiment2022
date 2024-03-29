from slack_sdk import WebClient
import os
import time

slack_token = os.environ["SLACK_BOT_TOKEN"]

client = WebClient(slack_token)


def send_message(message):

    response = client.chat_postMessage(
        channel="#test", text=message)


def get_channel_id(channel_name):
    for result in client.conversations_list():
        for channel in result["channels"]:
            if channel["name"] == channel_name:
                conversation_id = channel["id"]
                #print(f"found: {conversation_id}")
                return conversation_id
    return None


def get_channel_messages(channel_id, oldest="0"):
    conversation_history = []

    result = client.conversations_history(channel=channel_id, oldest=oldest)

    conversation_history = result["messages"]

    return conversation_history

    # print(conversation_history)
    #print("{} messages found in {}".format(len(conversation_history), channel_id))


if __name__ == "__main__":
    channel_name = input("channel name:")
    channel_id = get_channel_id(channel_name=channel_name)
    if channel_id is None:
        print("not found")
        exit()

    # NOTE: conversation_historyの引数oldestにはstr型を与えることになっている。
    # 小数点以下の桁数をちょうど6桁にしないと、チャンネル内メッセージのtimestampとうまく比較できないっぽい
    ts = str(round(time.time(), 6))
    while True:
        print("get message older than:", ts)
        con_hist = get_channel_messages(channel_id=channel_id, oldest=ts)
        new_message_flg = False
        if len(con_hist) != 0:
            for message in con_hist:
                if "bot_id" not in message:
                    print("\ttext:{}, ts:{}".format(message["text"], message["ts"]))
                    new_message_flg = True
        
        if new_message_flg == False:
            print("no new message")
        ts = str(round(time.time(), 6))
        time.sleep(10)
