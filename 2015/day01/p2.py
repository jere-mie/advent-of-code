inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().strip()
curr = 0
for i in range(len(text)):
    curr += 1 if text[i] == '(' else -1
    if curr == -1:
        print(i+1)
        exit()