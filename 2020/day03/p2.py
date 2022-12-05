lines = []
product=1
with open('input.txt', 'r') as f:
    for i in f:
        lines.append(i)

x = 0
trees = 0
for y in range(len(lines)):
    if lines[y][x]=='#':
        trees+=1
    x+=1
    if x >= 31:
        x-=31
print(trees)
product*=trees

x=0
trees=0
for y in range(len(lines)):
    if lines[y][x]=='#':
        trees+=1
    x+=3
    if x >= 31:
        x-=31
print(trees)
product*=trees

x=0
trees=0
for y in range(len(lines)):
    if lines[y][x]=='#':
        trees+=1
    x+=5
    if x >= 31:
        x-=31
print(trees)
product*=trees

x=0
trees=0
for y in range(len(lines)):
    if lines[y][x]=='#':
        trees+=1
    x+=7
    if x >= 31:
        x-=31
print(trees)
product*=trees

x=0
trees=0
for y in range(0, len(lines), 2):
    if lines[y][x]=='#':
        trees+=1
    x+=1
    if x >= 31:
        x-=31
print(trees)
product*=trees

print(product)