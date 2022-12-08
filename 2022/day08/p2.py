inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().splitlines()
    text = [list(map(int, list(i))) for i in text]

def seeRange(lst, target):
    dist = 0
    for i in range(len(lst)):
        dist+=1
        if lst[i]>=target:
            return dist
    return dist

def visible(i, j):
    l = text[i][:j]
    l.reverse()
    r = text[i][j+1:]
    col = [text[q][j] for q in range(len(text))]
    u = col[:i]
    u.reverse()
    d = col[i+1:]
    return seeRange(l, text[i][j])*seeRange(r, text[i][j])*seeRange(u, text[i][j])*seeRange(d, text[i][j])

newText = [[visible(i, j) for j in range(len(text[i]))] for i in range(len(text))]

print(max([max(i) for i in newText]))