import re

inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().splitlines()

parsed = []
id_sum = 0

pattern = r'Game (\d+): ([a-zA-Z0-9 ,;]+)'
for line in text:
    mat = re.search(pattern, line)
    id = mat.group(1)
    rest = [i.split(',') for i in mat.group(2).split(';')]
    rest = [[j.strip().split(' ') for j in i] for i in rest]
    parsed.append([id, rest])

for game in parsed:
    id = int(game[0])
    moves = game[1]
    maxes = dict()
    for round in moves:
        for colour in round:
            maxes[colour[1]] = max(int(colour[0]), maxes.get(colour[1], -1))
    if maxes['red'] <= 12 and maxes['green'] <= 13 and maxes['blue'] <= 14:
        id_sum+=id
print(id_sum)
