inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    data = [[i[0], int(i[1:])] for i in f.read().splitlines()]
pos = 50
times_at_0 = 0
for d in data:
    original_pos = pos
    if d[0] == 'L':
        for i in range(d[1]):
            pos -= 1
            if pos < 0:
                pos = 99
            if pos == 0:
                times_at_0 += 1
    if d[0] == 'R':
        for i in range(d[1]):
            pos += 1
            if pos >= 100:
                pos = 0
            if pos == 0:
                times_at_0 += 1
print(times_at_0)