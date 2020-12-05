import math
lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
ids = []

for i in lines:
    low=0
    high=127
    left=0
    right=7
    for j in range(7):
        if i[j]=='F':
            high = (low+high)//2
        elif i[j]=='B':
            low = math.ceil((low+high)/2)
    row = low
    for j in range(7,10):
        if i[j]=='L':
            right = (left+right)//2
        elif i[j]=='R':
            left = math.ceil((left+right)/2)
    col = left
    ids.append((row*8)+col)

ids.sort()
for i in range(len(ids)):
    if ids[i]-89!=i:
        print(i+89)
        break