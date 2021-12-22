import zipfile

with open('rockyou.txt', 'rb') as wordlist:
    for password in wordlist:
        if(len(password.strip()) == (24 * 4)):
            try:
                zipfile.ZipFile('geschenk.zip').extractall(pwd=password.strip())
            except:
                continue
            else:
                print('---------------------------------')
                print('Password found! \"' + password.decode().strip() + '\"')
                print('---------------------------------')
                exit(0)
print('Password could not be found')