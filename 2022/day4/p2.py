def overlap(l, r):
    if (l[0] <= r[0] and l[1] >= r[0]) or (r[0] <= l[0] and r[1] >= l[0]):
        return 1
    return 0

with open('input.txt', 'r') as f:
    pairs = list(map(lambda x:[x.split(',')[0].split('-'), x.split(',')[1].split('-')],f.read().splitlines()))
    pairs = [[[int(i) for i in j] for j in q] for q in pairs]
print(sum(map(lambda x:overlap(x[0], x[1]), pairs)))