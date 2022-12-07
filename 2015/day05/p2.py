
def containsPair(zain):
    for i in range(1, len(zain)):
        if zain[i-1:i+1] in zain[i+1:]:
            return True
    return False

def containsDouble(zain):
    for i in range(2, len(zain)):
        if zain[i]==zain[i-2]:
            return True
    return False

inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().splitlines()
    text = list(filter(containsPair, text))
    text = list(filter(containsDouble, text))
print(len(text))
