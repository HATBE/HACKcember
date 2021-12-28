import zipfile
from pathlib import Path
import shutil
import os
from PIL import Image, ImageChops
from tqdm import tqdm

def unzipPw(file, password):
    try:
        zipfile.ZipFile(file).extractall(pwd = bytes(password, 'utf-8'))
    except:
        print('Wrong Password')
        exit(1);
    os.remove(file)

Path("./work").mkdir(parents=True, exist_ok=True)
os.chdir('./work')
shutil.copy('../challenge.zip', './')

# PART 1
unzip = True
while(unzip):
    ls = os.listdir()
    for i in ls:
        if i == 'next_level.zip':
            unzip = False
            continue
        elif i.endswith('.zip'):
            try:
                zipfile.ZipFile(i).extractall();
                os.remove(i)
            except BaseException:
                pass
print('part 1 complete')

# PART 2
img1 = Image.open('A.png').convert('1') 
img2 = Image.open('B.png').convert('1') 
res = ImageChops.logical_xor(img1, img2)
res.show()

print('Please scan QR code!')
password = input('Input password: ')

os.remove('A.png')
os.remove('B.png')

unzipPw('next_level.zip', password)
print('part 2 complete')

# PART 3
with open('cybergedicht.txt') as f:
    text = f.read()
binStr = ''

for word in text.split():
    if 'cyber' in word.lower():
        if 'cyber-' in word.lower():
            binStr += '1'
        else:
            binStr += '0'

binInt = int(binStr, 2)
password = binInt.to_bytes((binInt.bit_length() + 7) // 8, 'big').decode()
os.remove('cybergedicht.txt')
unzipPw('fast_geschafft.zip', password)
print('part 3 complete')

# PART 4
with open('../rockyou.txt', 'rb') as wordlist:
    n = len(list(open('../rockyou.txt', "rb")))
    for password in tqdm(wordlist, total = n, unit = "passwords"):
        try:
            zipfile.ZipFile('flagge.zip').extractall(pwd=password.strip())
        except:
            continue
        else:
            os.remove('flagge.zip')            
            break
print('part 4 complete')

file = open('flagge.txt')
content = file.readlines()

print('Password: ' + content[3])