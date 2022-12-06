inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = list(map(lambda x: list(map(int, x.split('x'))), f.read().splitlines()))
    print(sum(map(lambda x:2*x[0]*x[1]+2*x[0]*x[2]+2*x[1]*x[2]+min([x[0]*x[1], x[0]*x[2], x[1]*x[2]]), text)))
