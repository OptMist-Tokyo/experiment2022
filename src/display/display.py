# -*- coding: utf-8 -*-
import socket,os
import subprocess,threading
from PIL import Image, ImageFont, ImageDraw
import time

LED_WIDTH = 64
LED_HEIGHT = 32

mu = threading.Lock()

def createPPM(text,color):
    global mu
    mu.acquire()

    # font = ImageFont.truetype("/usr/share/fonts/truetype/takao-mincho/TakaoMincho.ttf", LED_HEIGHT)  # (font, size)
    # font_path = "/usr/share/fonts/truetype/fonts-japanese-mincho.ttf"
    # font = ImageFont.truetype(font_path, LED_HEIGHT)  # (font, size)
    # whole_text = ""
    # for text_color_pair in text_color_pairs:
    #     whole_text += text_color_pair[0]
    
    proc = subprocess.Popen([f"exec /home/pi/experiment2022/src/rpi-rgb-led-matrix/examples-api-use/scrolling-text-example --led-cols=64 --led-rows=32 --led-chain=2 --led-no-hardware-pulse --led-slowdown-gpio=4 -l 2 -C{color[0]},{color[1]},{color[2]} -f /home/pi/Downloads/fonts/sazanami-20040629/sazanami-mincho.bdf \"{text}\""], shell = True)
    while proc.poll() is None:
        time.sleep(1)
    
    mu.release()

def display_string(text):
    return Popen([f"sudo /home/pi/experiment2022/src/rpi-rgb-led-matrix/examples-api-use/scrolling-text-example --led-cols=64 --led-rows=32 --led-chain=1 --led-no-hardware-pulse --led-slowdown-gpio=4 -t3 -f /home/pi/Downloads/fonts/sazanami-20040629/sazanami-mincho.bdf {text}"], shell = True)


if __name__ == "__main__":
    display_string("Hello World")