inpfile = 'input.txt'

with open(inpfile, 'r') as f:
    elves = f.read().split('\n\n')
elves = [i.split('\n') for i in elves]
elves = [[int(i) for i in j] for j in elves]

maxCals = max([sum(i) for i in elves])

print(maxCals)