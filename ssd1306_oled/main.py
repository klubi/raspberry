from ssd1306 import SSD1306_I2C
from machine import Pin, I2C

WIDTH = 128
HEIGHT = 32
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)


oled.fill(0)
oled.text('First line', 0, 0)
oled.text('Second line', 0, 17)
oled.show()
