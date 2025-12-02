import re
inpFile = 'input.txt'
pattern = r'(\d+)\[(\w+)\]'

with open(inpFile, 'r') as f:
    lines = [[i.split('-')[0:-1], re.search(pattern, i.split('-')[-1]).groups()] for i in f.read().splitlines()]
total = 0
for line in lines:
    name = ''.join(line[0])
    sectorID = int(line[1][0])
    checksum = line[1][1]

    counts = dict()
    for letter in name:
        if letter not in counts:
            counts[letter] = 0
        counts[letter] += 1
    # sort by count desc, letter asc
    sortedCounts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    calcChecksum = ''.join([i[0] for i in sortedCounts[0:5]])
    if calcChecksum == checksum:
        total += sectorID
print(total)
