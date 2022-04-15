from slack_sdk import WebClient

token = input("token:")

client = WebClient(token)

message = input("message:")

response = client.chat_postMessage(channel="#test", text=message, icon_emoji=":robot_face:")
