import machine

sdaPIN = machine.Pin(4)
sclPIN = machine.Pin(5)
i2c = machine.I2C(0, sda=sdaPIN, scl=sclPIN, freq=400000)

devices = i2c.scan()

if len(devices) == 0:
    print("No I2C device !")
else:
    print('I2C devices found:', len(devices))

for device in devices:
    print("I2C Address: ", hex(device))
