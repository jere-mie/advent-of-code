with open('input.txt', 'r') as f:
    lines = [[tuple(map(int, j.split(','))) for j in i.strip().split(' -> ')] for i in f.readlines()]

def isHor(line):
    return line[0][1]==line[1][1]

def isVert(line):
    return line[0][0]==line[1][0]


def walk(line):
    x1,x2,y1,y2 = 0,0,0,0
    out = []
    if isHor(line):
        if line[0][0]>=line[1][0]:
            x1,x2,y1,y2 = line[1][0],line[0][0],line[1][1],line[0][1]
        else:
            x2,x1,y2,y1 = line[1][0],line[0][0],line[1][1],line[0][1]            
        while x1<=x2:
            out.append((x1,y1))
            # print(f'{x1},{y1}')
            x1+=1
    elif isVert(line):
        if line[0][1]>=line[1][1]:
            x1,x2,y1,y2 = line[1][0],line[0][0],line[1][1],line[0][1]
        else:
            x2,x1,y2,y1 = line[1][0],line[0][0],line[1][1],line[0][1]
        while y1<=y2:
            out.append((x1,y1))
            # print(f'{x1},{y1} => {y2}')
            y1+=1
    return out

# print(walk([(1,1),(5,1)]))
# print(walk([(1,1),(1,5)]))
# print(isHor([(1,1),(1,5)]))
scores = dict()
for line in lines:
    points = walk(line)
    for point in points:
        if point in scores:
            scores[point]+=1
        else:
            scores[point]=1

num = 0
for point in scores:
    # print(f'{point} => {scores[point]}')
    if scores[point] >=2:
        num+=1
print(num)