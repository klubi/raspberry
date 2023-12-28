from mfrc522 import MFRC522
import utime

reader = MFRC522(spi_id=0, sck=6, miso=4, mosi=7, cs=5, rst=26)

try:
    while True:

        reader.init()
        (stat, tag_type) = reader.request(reader.REQIDL)
        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK:
                print("Card detected {}  uid={}".format(hex(int.from_bytes(
                    bytes(uid), "little", False)).upper(), reader.tohexstring(uid)))
        
        utime.sleep_ms(50)

except KeyboardInterrupt:
    pass