import secrets
inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().split("$ cd ")
sizes = dict()
text = list(filter(lambda x:x!='..\n', text))
text = [i.replace('$ ls\n', '') for i in text]
text = [i.split('\n') for i in text]
text = [list(filter(lambda x:x!='', i)) for i in text]
text = list(filter(lambda x: x!=[], text))

tot = 0
dirTotals = []
def processFolder(fname, index):
    print(fname)
    # find first occurence of the folder
    curr = 0
    global tot
    global dirTotals
    for i in range(index, len(text)):
        if text[i][0] == fname:
            print('found', fname, i)
            # we now recursively return sum
            for j in text[i][1:]:
                if j[:4] == 'dir ':
                    print("processing", j[4:], i)
                    curr+=processFolder(j[4:], i)
                else:
                    curr+=int(j.split(' ')[0])
            if curr <= 100000:
                tot+=curr
            text[i][0] = secrets.token_hex(13)
            dirTotals.append(curr)
            return curr
    return 0

total = processFolder('/', 0)
objective = 30000000-(70000000-total)
print(objective)
dirTotals = sorted(dirTotals)
print(dirTotals)
for i in dirTotals:
    if i>=objective:
        print(i)
        exit()
