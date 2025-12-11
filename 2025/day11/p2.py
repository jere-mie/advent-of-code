import functools
inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    data = [i.split(':') for i in f.read().splitlines()]
data = {i[0]: i[1].strip().split(' ') for i in data}

@functools.cache
def traverse(node):
    if node == 'out':
        return 0
    elif node == 'fft':
        return sum(traverse_fft_found(i) for i in data[node])
    elif node == 'dac':
        return sum(traverse_dac_found(i) for i in data[node])
    return sum(traverse(i) for i in data[node])

@functools.cache
def traverse_fft_found(node):
    if node == 'out':
        return 0
    elif node == 'dac':
        return sum(traverse_fft_and_dac_found(i) for i in data[node])
    return sum(traverse_fft_found(i) for i in data[node])

@functools.cache
def traverse_dac_found(node):
    if node == 'out':
        return 0
    elif node == 'fft':
        return sum(traverse_fft_and_dac_found(i) for i in data[node])
    return sum(traverse_dac_found(i) for i in data[node])

@functools.cache
def traverse_fft_and_dac_found(node):
    if node == 'out':
        return 1
    return sum(traverse_fft_and_dac_found(i) for i in data[node])

print(traverse('svr'))
