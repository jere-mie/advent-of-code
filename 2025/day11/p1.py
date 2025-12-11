inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    data = [i.split(':') for i in f.read().splitlines()]
data = {i[0]: i[1].strip().split(' ') for i in data}

def traverse(node):
    if node == 'out':
        return 1
    return sum(traverse(i) for i in data[node])

print(traverse('you'))
