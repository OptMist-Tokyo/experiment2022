# -*- coding: utf-8 -*-
import socket
from subprocess import Popen
from PIL import Image, ImageFont, ImageDraw
import time

LED_WIDTH = 64
LED_HEIGHT = 32


def createPPM(text_color_pairs):    # メッセージを ppm ファイルに変換
    # font = ImageFont.truetype("/usr/share/fonts/truetype/takao-mincho/TakaoMincho.ttf", LED_HEIGHT)  # (font, size)
    font_path = "/usr/share/fonts/truetype/fonts-japanese-mincho.ttf"
    font = ImageFont.truetype(font_path, LED_HEIGHT)  # (font, size)
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
    return Popen([f"sudo /home/pi/experiment2022/src/rpi-rgb-led-matrix/examples-api-use/scrolling-text-example --led-cols=64 --led-rows=32 --led-chain=2 --led-no-hardware-pulse --led-slowdown-gpio=2 -f /home/pi/Downloads/fonts/sazanami-20040629/sazanami-mincho.bdf {whole_text}"], shell = True)
    # return Popen(["exec /home/pi/experiment2022/src/rpi-rgb-led-matrix/examples-api-use/demo --led-no-hardware-pulse --led-rows=32 --led-cols=64 -D 1 -zm 20 -f /home/pi/Downloads/fonts/sazanami-20040629/sazanami-mincho.bdf "], shell = True)  # "shell = True" is needed only when you use Windows
    time.sleep(5)   # show display for 10 seconds before exit


if __name__ == "__main__":
    createPPM([
        ["あいうえお", [255, 255, 0]],
        ["あいうえお", [0, 255, 255]],
        ["あいうえお", [255, 0, 255]]])
