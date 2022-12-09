inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = [[i[:1], int(i[2:])] for i in f.read().splitlines()]

# x, y
head = [0, 0]
tail = [0, 0]
visited = set()
visited.add(tuple(tail))

for i in text:
    for j in range(i[1]):
        match i[0]:
            case 'U':
                if head[1]>tail[1]:
                    tail = [head[0], head[1]]
                    visited.add(tuple(tail))
                head[1]+=1
            case 'D':
                if head[1]<tail[1]:
                    tail = [head[0], head[1]]
                    visited.add(tuple(tail))
                head[1]-=1
            case 'L':
                if head[0]<tail[0]:
                    tail = [head[0], head[1]]
                    visited.add(tuple(tail))
                head[0]-=1
            case 'R':
                if head[0]>tail[0]:
                    tail = [head[0], head[1]]
                    visited.add(tuple(tail))
                head[0]+=1
print(len(visited))
