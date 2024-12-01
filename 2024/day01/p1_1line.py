print(sum([abs(l[0]-l[1]) for l in zip(*[sorted(list(k)) for k in zip(*[[int(j) for j in i.split('   ')] for i in open('input.txt', 'r').read().splitlines()])])]))
