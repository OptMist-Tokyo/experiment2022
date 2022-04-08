from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (512, 512)
camera.start_preview()
camera.start_recording('/home/pi/experiment2022/sample/sample_video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()