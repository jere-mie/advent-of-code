inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    ranges = [(int(i.split('-')[0]), int(i.split('-')[1])) for i in f.read().strip().split(',')]

total = 0
for r in ranges:
    a = r[0]
    b = r[1]
    for i in range(a, b + 1):
        string = str(i)
        # split in half
        left = string[:len(string)//2]
        right = string[len(string)//2:]
        if left == right:
            total += i
print(total)
