inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().strip()
seen = set([(0, 0)])
# x, y
santa = [0, 0]
robo = [0, 0]
# santa
for i in range(0, len(text), 2):
    match text[i]:
        case '^':
            santa[1]+=1
        case 'v':
            santa[1]-=1
        case '<':
            santa[0]-=1
        case '>':
            santa[0]+=1
    seen.add(tuple(santa))
# robo
for i in range(1, len(text), 2):
    match text[i]:
        case '^':
            robo[1]+=1
        case 'v':
            robo[1]-=1
        case '<':
            robo[0]-=1
        case '>':
            robo[0]+=1
    seen.add(tuple(robo))
print(len(seen))
