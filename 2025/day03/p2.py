inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    lists = [[int(j) for j in list(i)] for i in f.read().splitlines()]

total = 0
for listi in lists:
    nums = []
    idx = -1
    for i in range(12):
        a = max(listi[:-11+i] if i!=11 else listi)
        idx = listi.index(a)
        nums.append(a)
        listi = listi[idx+1:]
    total+=int(''.join(map(str, nums)))
print(total)
