inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    lists = [[int(j) for j in list(i)] for i in f.read().splitlines()]

total = 0
for listi in lists:
    a = max(listi[:-1])
    idx = listi.index(a)
    b = max(listi[idx+1:])
    total+=int(f'{a}{b}')
print(total)
