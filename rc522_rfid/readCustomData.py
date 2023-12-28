import utime
from mfrc522 import MFRC522

reader = MFRC522(spi_id=0, sck=6, miso=4, mosi=7, cs=5, rst=26)
blockToReadFrom = 8

def blockToString(block):
    return "".join(chr(int(value[2:], 16)) for value in block if int(value[2:], 16)> 0x20 and int(value[2:], 16) < 0x7f)

print("")
print("Please place card on reader")
print("")


try:
    while True:

        reader.init()
        (stat, tag_type) = reader.request(reader.REQIDL)
        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            defaultKey = [255, 255, 255, 255, 255, 255]
            status, block = reader.readSectorBlock(uid, blockToReadFrom/4, blockToReadFrom % 4, keyA=defaultKey)
            if status == MFRC522.OK:
                print(blockToString(block))

        utime.sleep_ms(50)

except KeyboardInterrupt:
    pass