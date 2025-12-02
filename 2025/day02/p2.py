inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    ranges = [(int(i.split('-')[0]), int(i.split('-')[1])) for i in f.read().strip().split(',')]

total = 0
for r in ranges:
    a = r[0]
    b = r[1]
    for i in range(a, b + 1):
        string = str(i)
        len_s = len(string)
        # see if repeat of 1, 2, 3 up to half the length
        for l in range(1, len_s // 2 + 1):
            if len_s % l == 0:
                pattern = string[:l]
                if pattern * (len_s // l) == string:
                    total += i
                    break
print(total)
