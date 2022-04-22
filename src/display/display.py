import socket
from subprocess import Popen
from PIL import Image, ImageFont, ImageDraw

LED_WIDTH = 64
LED_HEIGHT = 32


def createPPM(text_color_pairs):    # 受信したデータを元に ppm ファイルを作成
    # font = ImageFont.truetype("/usr/share/fonts/truetype/takao-mincho/TakaoMincho.ttf", LED_HEIGHT)  # (font, size)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", LED_HEIGHT)  # (font, size)
    whole_text = ""
    for text_color_pair in text_color_pairs:
        whole_text += text_color_pair[0]

    width, height = font.getsize(whole_text)
    im = Image.new("RGB", (width+30, LED_HEIGHT), "black")   # (mode, size(width, height), background color)
    draw = ImageDraw.Draw(im)

    x = 0
    for text_color_pair in text_color_pairs:
        text = text_color_pair[0]
        color = tuple(text_color_pair[1])
        draw.text((x, 0), text, color, font=font)
        x += font.getsize(text)[0]

    im.save("/home/pi/message.ppm")
    return Popen(["exec /home/pi/experiment2022/src/rpi-rgb-led-matrix/examples-api-use/demo --led-no-hardware-pulse --led-rows=32 --led-cols=64 -D 1 -m 20 /home/pi/message.ppm"], shell = True)  # "shell = True" is needed only when you use Windows


# TODO: 日本語用のフォントを "/usr/share/fonts/truetype/" にダウンロード
createPPM([
    ["さくさく", [255, 255, 0]],
    ["ラズベリーパイ", [0, 255, 255]],
    ["を焼こう！", [255, 0, 255]]])
