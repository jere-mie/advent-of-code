inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = [i.split(',') for i in f.read().splitlines()]

directions = [[[j[0], int(j[1:])] for j in i] for i in text]

coords = [set(), set()]
coords_withsteps = [dict(), dict()]
for idx, path in enumerate(directions):
    x, y = 0, 1
    curr = [0, 0]
    steps=0
    for j in path:
        dir = j[0]
        dist = j[1]
        if dir == 'U':
            for _ in range(dist):
                steps+=1
                curr[y]+=1
                coords[idx].add(tuple(curr))
                coords_withsteps[idx][tuple(curr)] = min([steps, coords_withsteps[idx].get(tuple(curr), 99999999999)])
        elif dir == 'D':
            for _ in range(dist):
                steps+=1
                curr[y]-=1
                coords[idx].add(tuple(curr))
                coords_withsteps[idx][tuple(curr)] = min([steps, coords_withsteps[idx].get(tuple(curr), 99999999999)])
        elif dir == 'L':
            for _ in range(dist):
                steps+=1
                curr[x]-=1
                coords[idx].add(tuple(curr))
                coords_withsteps[idx][tuple(curr)] = min([steps, coords_withsteps[idx].get(tuple(curr), 99999999999)])
        elif dir == 'R':
            for _ in range(dist):
                steps+=1
                curr[x]+=1
                coords[idx].add(tuple(curr))
                coords_withsteps[idx][tuple(curr)] = min([steps, coords_withsteps[idx].get(tuple(curr), 99999999999)])
        else:
            print("WTF???")
            exit(1)

crosses = list(coords[0]&coords[1])
steps = [coords_withsteps[0][i]+coords_withsteps[1][i] for i in crosses]
print(min(steps))