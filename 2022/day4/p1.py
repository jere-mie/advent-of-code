with open('test.txt', 'r') as f:
    pairs = list(map(lambda x:[x.split(',')[0].split('-'), x.split(',')[1].split('-')],f.read().splitlines()))
for i in pairs:
    l, r = i
    print(l, r)