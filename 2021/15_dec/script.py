import binascii

with open('text.txt') as f:
    text = f.read()

binStr = ''

for word in text.split():
    if 'cyber' in word.lower():
        if 'cyber-' in word.lower():
            binStr += '1'
        else:
            binStr += '0'

binInt = int(binStr, 2)
res = binInt.to_bytes((binInt.bit_length() + 7) // 8, 'big').decode()
print('----------------------------------------------')
print('The Password is: \"' + res + "\"")
print('----------------------------------------------')