inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    data = [list(j) for j in zip(*[list(i) for i in f.read().splitlines()])]
message = ''
for datum in data:
    message += min([f'{datum.count(char):05d}_{char}' for char in set(datum)]).split('_')[1]
print(message)