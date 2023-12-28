from mfrc522 import MFRC522

'''
BE AWARE that sectors(3,7,11,15,...,63) are access block.
if you want to change  (sector % 4) == 3 you should
know how defaultKeys and permission work!
'''


def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring


reader = MFRC522(spi_id=0, sck=6, miso=4, mosi=7, cs=5, rst=26)


defaultKey = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
blockToWriteTo = 8
stringToWrite = "klubi!"

# This will trim string to 16 characters

def stringToHexTable(stringToWrite):
    return [hex(ord(a)) for a in stringToWrite[:16]]


print("")
print("Please place card on reader")
print("")

try:
    while True:

        (stat, tag_type) = reader.request(reader.REQIDL)

        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK:
                print(uid)
                print("Card detected %s" % uidToString(uid))
                reader.MFRC522_DumpClassic1K(uid, keyA=defaultKey)
                value = stringToHexTable(stringToWrite)
                for i in range(16-len(value)):
                    value.append(i)
                print("Test ! writing absolute block({})".format(blockToWriteTo))
                print("with {} [{}]".format(stringToWrite, value))
                status = reader.auth(reader.AUTHENT1A, blockToWriteTo, defaultKey, uid)
                if status == reader.OK:
                    status = reader.write(blockToWriteTo, value)
                    if status == reader.OK:
                        reader.MFRC522_DumpClassic1K(uid, keyA=defaultKey)
                    else:
                        print("unable to write")
                else:
                    print("Authentication error for writing")
                break
except KeyboardInterrupt:
    print("Bye")
