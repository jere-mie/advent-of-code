inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    data = [[int(j) for j in i.split(' ')] for i in f.read().splitlines()]
    data = list((i) for i in zip(*data))

valid_count = 0

for datum in data:
    for i in range(0, len(datum), 3):
        triangle = sorted([datum[i], datum[i+1], datum[i+2]])
        if triangle[0] + triangle[1] > triangle[2]:
            valid_count += 1
print(valid_count)
