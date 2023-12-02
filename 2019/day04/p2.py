inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    lower, upper = tuple([int(i) for i in f.read().split('-')])

def countainsDouble(num):
    doubles = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']
    triples = ['000', '111', '222', '333', '444', '555', '666', '777', '888', '999']

    for s in range(len(doubles)):
        if doubles[s] in str(num) and triples[s] not in str(num):
            return True
    return False

def digitsDontDecrease(num):
    digit_list = [int(i) for i in list(str(num))]
    for i in range(len(digit_list)-1):
        if digit_list[i] > digit_list[i+1]:
            return False
    return True
def isPassValid(num):
    if not countainsDouble(num):
        return False
    if not digitsDontDecrease(num):
        return False
    return True

count = 0
for i in range(lower, upper+1):
    if isPassValid(i):
        count+=1
print(count)