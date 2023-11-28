from machine import Pin
import utime

pir = Pin(0, Pin.IN, Pin.PULL_DOWN)

print('Starting up the PIR Module')
utime.sleep(1)
print('Ready')

while True:
    if pir.value() == 1:
        print('Motion Detected ')

    utime.sleep(1)
