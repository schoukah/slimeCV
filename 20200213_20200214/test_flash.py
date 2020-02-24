"""
Copyright 2013-2015 Dave Jones

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
- Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


First tests performed on 2020-02-13 and following by Sarah Choukah

Taken from: Picamera docs
https://picamera.readthedocs.io/en/release-1.10/recipes1.html#capturing-in-low-light

"""

from gpiozero import LED
from time import sleep
from picamera import PiCamera
from os import system
import datetime
import time
from fractions import Fraction

led = LED(14)
led2 = LED(15)

# take photo with 3 second exposure set at 1/3fps
camera = PiCamera(
    resolution=(1280,720),
    framerate=Fraction(1, 3),
    sensor_mode=3)
camera.shutter_speed = 3000000
camera.iso = 800

# letting the camera start and adjust
sleep(30)
camera.exposure_mode = 'off'


# Take 480 photos while activating the LEDs for 50 seconds
# In total a little over 8 hours
for i in range(480):
    led.on() 
    led2.on()
    sleep(15)
    camera.capture('slimeLapse{0:04d}.jpg'.format(i))
    led.off()
    led2.off()
    sleep(60)
    
sleep(6)
camera.close()

## Variations for timed flash:
## Following code block will light leds off and on for a minute at a specific
## hour and minute of the day.
## To use if need for taking pics at a specific time of day:

## while True:
#     time_1 = datetime.datetime.now().strftime("%H:%M")
#     if time_1 == "13:19":
#         led.on()
#         led2.on()
#         sleep(10)
#         led.off()
#         led2.off()
#     time.sleep(0.030)
    
