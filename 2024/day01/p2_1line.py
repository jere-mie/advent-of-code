print(sum(list([l[0][m]*(sum([1 if n==l[0][m] else 0 for n in l[1]])) for m in range(len(l[0]))] for l in [[list(k) for k in zip(*[[int(j) for j in i.split('   ')] for i in open('input.txt', 'r').read().splitlines()])]])[0]))