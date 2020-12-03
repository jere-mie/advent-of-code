lines = []
with open('input.txt', 'r') as f:
    for i in f:
        lines.append(i)
x = 0
trees = 0
for y in range(len(lines)):
    if lines[y][x]=='#':
        trees+=1
    x+=3
    if x >= 31:
        x-=31
print(trees)