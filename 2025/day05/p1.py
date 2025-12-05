inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    ranges, ids = [i.split('\n') for i in f.read().split('\n\n')]

ranges = [tuple(map(int, r.split('-'))) for r in ranges]
ids = [int(i) for i in ids]

tot = 0
for i in ids:
    if any(r[0] <= i <= r[1] for r in ranges):
        tot += 1
print(tot)
