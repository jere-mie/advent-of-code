import re

inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    matrix = f.read().splitlines()

partSum = 0

def isDigitOrDot(s):
    return s.isdigit() or s=='.'

def matGet(x, y, matrix):
    if x > len(matrix[0])-1 or x < 0 or y > len(matrix)-1 or y < 0:
        return '.'
    return matrix[y][x]

def digitAdjacentToSymbol(x, y, matrix):
    if not isDigitOrDot(matGet(x-1, y, matrix)): # left
        return True
    elif not isDigitOrDot(matGet(x+1, y, matrix)): # right
        return True
    elif not isDigitOrDot(matGet(x, y-1, matrix)): # up
        return True
    elif not isDigitOrDot(matGet(x, y+1, matrix)): # down
        return True
    elif not isDigitOrDot(matGet(x-1, y-1, matrix)): # up left
        return True
    elif not isDigitOrDot(matGet(x+1, y-1, matrix)): # up right
        return True
    elif not isDigitOrDot(matGet(x-1, y+1, matrix)): # down left
        return True
    elif not isDigitOrDot(matGet(x+1, y+1, matrix)): # down right
        return True
    return False

def numberAdjacentToSymbol(x1, x2, y, matrix):
    for x in range(x1, x2):
        if digitAdjacentToSymbol(x, y, matrix):
            return True
    return False

def findNumbers(line):
    matches = re.finditer(r'\d+', line)
    nums = [(match.start(), match.end(), int(match.group())) for match in matches]
    return nums

for idx, line in enumerate(matrix):
    nums = findNumbers(line)
    for num in nums:
        if numberAdjacentToSymbol(num[0], num[1], idx, matrix):
            partSum+=num[2]
print(partSum)
