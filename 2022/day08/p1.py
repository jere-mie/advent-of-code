inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().splitlines()
    text = [list(map(int, list(i))) for i in text]
        
def visibleup(i, j):
    # base case
    if i==0:
        return True
    # check up
    for q in range(0, i):
        if text[i][j] <= text[q][j]:
            return False
    return True

def visibledown(i, j):
    # base case
    if i==len(text)-1:
        return True
    # check down
    for q in range(i+1, len(text)):
        if text[i][j] <= text[q][j]:
            return False
    return True

def visibleleft(i, j):
    # base case
    if j==0:
        return True
    # check left
    for q in range(0, j):
        if text[i][j] <= text[i][q]:
            return False
    return True

def visibleright(i, j):
    # base case
    if j==len(text[i])-1:
        return True
    # check right
    for q in range(j+1, len(text[i])):
        if text[i][j] <= text[i][q]:
            return False
    return True

def visible(i, j):
    return visibleup(i, j) or visibledown(i, j) or visibleleft(i, j) or visibleright(i, j)

newText = [[1 if visible(i, j) else 0 for j in range(len(text[i]))] for i in range(len(text))]
tot = sum([sum(i) for i in newText])
print(tot)