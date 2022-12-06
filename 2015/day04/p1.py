import hashlib

inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().strip()
i = 1
while True:
    res = hashlib.md5(f"{text}{i}".encode()).hexdigest()
    if res[:5] == '00000':
        print(i)
        exit()
    i+=1
