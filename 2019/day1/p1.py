from math import floor
from functools import reduce
with open('input.txt', 'r') as f:
    print(reduce(lambda a,b: a+floor(b/3)-2, [0]+list(map(int, f.readlines()))))