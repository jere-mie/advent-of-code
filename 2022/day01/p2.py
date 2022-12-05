inpfile = 'input.txt'

with open(inpfile, 'r') as f:
    elves = f.read().split('\n\n')
elves = [i.split('\n') for i in elves]
elves = [[int(i) for i in j] for j in elves]

elves = [sum(i) for i in elves]
elves = sorted(elves)
maxCals = sum(elves[-3:])

print(maxCals)