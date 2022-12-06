def sumVowels(zain):
    l = list(zain)
    return sum(map(lambda x: 1 if x in {'a', 'e', 'i', 'o', 'u'} else 0, l)) >= 3

def containsDouble(zain):
    for i in range(1, len(zain)):
        if zain[i]==zain[i-1]:
            return True
    return False

def containsBadStr(zain):
    return not ('ab' in zain or 'cd' in zain or 'pq' in zain or 'xy' in zain)

inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().splitlines()
    text = list(filter(sumVowels, text))
    text = list(filter(containsDouble, text))
    text = list(filter(containsBadStr, text))
print(len(text))
