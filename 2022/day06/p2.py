inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().strip()
for i in range(13, len(text)):
    temp = text[i-13:i+1]
    if len(set(temp)) == 14:
        print(i+1)
        exit()