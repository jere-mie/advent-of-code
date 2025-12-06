import re
inpFile = 'input.txt'

with open(inpFile, 'r') as f:
    data = [[int(q) if q.isnumeric() else q for q in j] for j in zip(*[i.strip().split(' ') for i in re.sub(' +', ' ', f.read()).strip().splitlines()])]

tot = 0
for row in data:
    if row[-1] == '+':
        tot += sum(row[:-1])
    elif row[-1] == '*':
        prod = 1
        for num in row[:-1]:
            prod *= num
        tot += prod
print(tot)