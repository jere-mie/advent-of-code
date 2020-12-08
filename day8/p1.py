import re
lines = []
instructs = []
acc = 0
prev = set()
loc = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()

instructs = []
for line in lines:
    instructs.append(re.findall(r'(jmp|acc|nop) (\+|-)(\d+)', line)[0])

while True:
    if loc in prev:
        print(acc)
        break
    prev.add(loc)
    line = instructs[loc]
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