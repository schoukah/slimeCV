from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

#camera warm-up time
sleep(2)
camera.capture('firstScriptTest.jpg')
