inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().strip()
seen = set([(0, 0)])
# x, y
curr = [0, 0]
for i in text:
    match i:
        case '^':
            curr[1]+=1
        case 'v':
            curr[1]-=1
        case '<':
            curr[0]-=1
        case '>':
            curr[0]+=1
    seen.add(tuple(curr))
print(len(seen))
