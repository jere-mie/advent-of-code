inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = [i.split(',') for i in f.read().splitlines()]

directions = [[[j[0], int(j[1:])] for j in i] for i in text]

coords = [set(), set()]
for idx, path in enumerate(directions):
    x, y = 0, 1
    curr = [0, 0]
    for j in path:
        dir = j[0]
        dist = j[1]
        if dir == 'U':
            for _ in range(dist):
                curr[y]+=1
                coords[idx].add(tuple(curr))
        elif dir == 'D':
            for _ in range(dist):
                curr[y]-=1
                coords[idx].add(tuple(curr))
        elif dir == 'L':
            for _ in range(dist):
                curr[x]-=1
                coords[idx].add(tuple(curr))
        elif dir == 'R':
            for _ in range(dist):
                curr[x]+=1
                coords[idx].add(tuple(curr))
        else:
            print("WTF???")
            exit(1)

crosses = list(coords[0]&coords[1])
distances = [abs(i[0])+abs(i[1]) for i in crosses]
print(min(distances))