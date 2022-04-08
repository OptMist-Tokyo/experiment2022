from gpiozero import PWMLED

led = PWMLED(14)

while True:
    brightness_s = input("Enter Brightness (0.0 to 1.0):")
    brigtness = float(brightness_s)
    led.value = brigtness
