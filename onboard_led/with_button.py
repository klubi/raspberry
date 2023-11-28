#Simple example of changing onboard LED color using neopixel lib, and single tactile switch
import neopixel
import random
from machine import Pin
from picozero import Button

button = Button(0)

led_pin = Pin(16)
led = neopixel.NeoPixel(led_pin, 1)

def change_led():
    led[0] = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    led.write()

button.when_pressed = change_led