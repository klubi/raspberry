#Simple example of changing onboard LED color using neopixel library

import neopixel
import utime
from machine import Pin

led_pin = Pin(16)
led = neopixel.NeoPixel(led_pin, 1)

while True:
    for r in range(10):
        led[0] = (r*8, 0, 0)

        led.write()
        utime.sleep(.2)
