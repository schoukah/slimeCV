from picamera import PiCamera
from os import system
from time import sleep

camera = PiCamera()
camera.resolution = (256, 192)

for i in range(10):
    camera.capture('image{0:04d}.jpg'.format(i))
    sleep(10)

system('convert -delay 10 -loop 0 image*.jpg animation.gif')
