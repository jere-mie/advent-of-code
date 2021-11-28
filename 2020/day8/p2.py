def test(changed, instructs):
    newinstr = []
    for i in range(len(instructs)):
        newinstr.append(instructs[i])
    if newinstr[changed][0] == 'nop':
        newinstr[changed] = ('jmp', newinstr[changed][1], newinstr[changed][2])
    elif newinstr[changed][0] =='jmp':
        newinstr[changed] = ('nop', newinstr[changed][1], newinstr[changed][2])
    loc=0
    acc=0
    prev = set()
    while True:
        if loc == len(newinstr):
            print(acc)
            return 1
        elif loc > len(newinstr):
            return -1
        if loc in prev:
            return 0
        prev.add(loc)
        line = newinstr[loc]
        if line[0] == 'acc':
            if line[1] == '+':
                acc+=int(line[2])
            else:
                acc-=int(line[2])
            loc+=1
        elif line[0] == 'nop':
            loc+=1
        elif line[0] == 'jmp':
            if line[1] == '+':
                loc+=int(line[2])
            else:
                loc-=int(line[2])

import re
lines = []
instructs = []
acc = 0
prev = set()
prevTested = set()
loc = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()

instructs = []
for line in lines:
    instructs.append(re.findall(r'(jmp|acc|nop) (\+|-)(\d+)', line)[0])

for i in range(len(instructs)):
    if instructs[i][0] == 'nop' or instructs[i][0] == 'jmp':
        result = test(i, instructs)
        if result == '1':
            break