import hashlib

def md5(s):
    m = hashlib.md5()
    m.update(s.encode('utf-8'))
    return m.hexdigest()


inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().strip()

i = 0
password = ['' for _ in range(8)]
while len(''.join(password)) < 8:
    test_str = f"{text}{i}"
    hash = md5(test_str)
    if hash.startswith('00000') and hash[5] in '01234567' and password[int(hash[5])] == '':
        print(f"Found: {i}")
        password[int(hash[5])] = hash[6]
    i += 1
print(f"Password: {''.join(password)}")