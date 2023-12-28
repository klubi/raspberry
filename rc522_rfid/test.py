
# This test should always be able to turn string into table of char hex values, and then back again

someString = "klubi"

def stringToHexTable(stringToWrite):
    return [hex(ord(a)) for a in stringToWrite[:16]]

def blockToString(block):
    return "".join(chr(int(value[2:], 16)) for value in block if int(value[2:], 16)> 0x20 and int(value[2:], 16) < 0x7f)

hexStr = stringToHexTable(someString)
print(hexStr)
somestr = blockToString(hexStr)
print(somestr)