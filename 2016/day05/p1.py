import hashlib

def md5(s):
    m = hashlib.md5()
    m.update(s.encode('utf-8'))
    return m.hexdigest()

inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().strip()

i = 0
password = ''
while len(password) < 8:
    test_str = f"{text}{i}"
    if md5(test_str).startswith('00000'):
        password += md5(test_str)[5]
    i += 1
print(password)
