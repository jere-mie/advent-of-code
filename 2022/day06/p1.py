inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().strip()
for i in range(3, len(text)):
    temp = text[i-3:i+1]
    if len(set(temp)) == 4:
        print(i+1)
        exit()