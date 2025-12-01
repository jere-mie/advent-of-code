inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    moves = [(i[0], int(i[1:])) for i in f.read().split(', ')]
x = 0
y = 0
dirs = ['N', 'E', 'S', 'W']
dir = 0

for direction, distance in moves:
    # get current direction
    if direction == 'R':
        dir = (dir+1)%4
    else:
        dir = (4+((dir-1)))%4

    # apply distance
    if dirs[dir] == 'N':
        y+=distance
    elif dirs[dir] == 'E':
        x+=distance
    elif dirs[dir] == 'S':
        y-=distance
    elif dirs[dir] == 'W':
        x-=distance
print(abs(x)+abs(y))