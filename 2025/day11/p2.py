import functools
inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    data = [i.split(':') for i in f.read().splitlines()]
data = {i[0]: i[1].strip().split(' ') for i in data}

@functools.cache
def traverse(node, fft_found, dac_found):
    if node == 'out':
        return 1 if fft_found and dac_found else 0
    elif node == 'fft':
        return sum(traverse(i, True, dac_found) for i in data[node])
    elif node == 'dac':
        return sum(traverse(i, fft_found, True) for i in data[node])
    return sum(traverse(i, fft_found, dac_found) for i in data[node])

print(traverse('svr', False, False))
