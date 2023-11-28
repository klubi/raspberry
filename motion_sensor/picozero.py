import utime
from picozero import DigitalInputDevice

sensor = DigitalInputDevice(0, pull_up = False)

print('Starting up the PIR Module')
utime.sleep(1)
print('Ready')

while True:
    if sensor.is_active:
        print("Motion detected")

    utime.sleep(1)
