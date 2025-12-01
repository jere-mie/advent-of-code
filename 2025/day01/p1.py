inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    data = [[i[0], int(i[1:])] for i in f.read().splitlines()]
pos = 50
times_at_0 = 0
for d in data:
    if d[0] == 'L':
        pos -= d[1]
    if d[0] == 'R':
        pos += d[1]
    while pos < 0:
        pos += 100
    while pos >= 100:
        pos -= 100
    if pos == 0:
        times_at_0 += 1
print(times_at_0)