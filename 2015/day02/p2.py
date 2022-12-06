inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = list(map(lambda x: list(map(int, x.split('x'))), f.read().splitlines()))
    text = [sorted(i) for i in text]
    print(sum([2*(i[0]+i[1]) + i[0]*i[1]*i[2] for i in text]))
