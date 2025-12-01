inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    moves = [(i[0], int(i[1:])) for i in f.read().split(', ')]
x = 0
y = 0
dirs = ['N', 'E', 'S', 'W']
dir = 0

visited = [(0, 0)]

for direction, distance in moves:
    # get current direction
    if direction == 'R':
        dir = (dir+1)%4
    else:
        dir = (4+((dir-1)))%4

    # apply distance and track visited locations
    if dirs[dir] == 'N':
        visited += [(x, y+i) for i in range(1, distance+1)]
        y+=distance
    elif dirs[dir] == 'E':
        visited += [(x+i, y) for i in range(1, distance+1)]
        x+=distance
    elif dirs[dir] == 'S':
        visited += [(x, y-i) for i in range(1, distance+1)]
        y-=distance
    elif dirs[dir] == 'W':
        visited += [(x-i, y) for i in range(1, distance+1)]
        x-=distance
    # check for duplicates
    dupes = [i for i in visited if visited.count(i) > 1]
    if dupes:
        print("Visited twice:", dupes[0])
        print(abs(dupes[0][0]) + abs(dupes[0][1]))
        exit()
