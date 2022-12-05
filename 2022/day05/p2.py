import re

# getting input
inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    stack, moves = f.read().split('\n\n')
stack = stack.splitlines()
moves = moves.splitlines()

# getting stacks
numStacks = (len(stack[0])+1)//4
stacks = [[] for i in range(numStacks)]
for i in range(len(stack[-1])):
    if stack[-1][i].isnumeric():
        num = int(stack[-1][i])-1
        for q in range(len(stack)-1, -1, -1):
            if stack[q][i].isalpha():
                stacks[num].append(stack[q][i])
# getting moves
moves = list(map(lambda x: list(map(int, list(re.match(r'move (\d+) from (\d+) to (\d+)', x).groups()))), moves))

# simulating moves
for i in moves:
    snum, sfrom, sto  = i
    stacks[sfrom-1], stacks[sto-1] = stacks[sfrom-1][:-snum], stacks[sto-1]+stacks[sfrom-1][-snum:] 

# printing
for i in stacks:
    print(i.pop(), end="")
print()
