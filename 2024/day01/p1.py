inpFile = 'test.txt'
with open(inpFile, 'r') as f:
    text = f.read().splitlines()
print(text)
