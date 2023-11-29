from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd
import utime

i2c_address = 0x27
i2c_rows_count = 2
i2c_cols_count = 16

i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
lcd = I2cLcd(i2c, i2c_address, i2c_rows_count, i2c_cols_count)

for count in range(0, 5):
    lcd.move_to(0, 0)
    lcd.putstr(f"Count: {count}")
    lcd.move_to(0, 1)
    lcd.putstr(f"Count square: {count*count}")
    utime.sleep(1)
