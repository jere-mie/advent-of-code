"""

THIS IS UNFINISHED
THERE'S LOTS OF GARBAGE CODE IN HERE RIGHT NOW
I'LL FINISH THIS... AT SOME POINT
JUST PUSHING THIS CODE FOR WHEN I COME BACK TO IT

"""

import re

inpFile = 'test.txt'
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
        # print(f'checking {x}, {y} for {matrix[y][x1:x2+1]}')
        if digitAdjacentToSymbol(x, y, matrix):
            return True
    return False


def findStars(line):
    matches = re.finditer(r'[*]', line)
    stars = [match.start() for match in matches]
    return stars    

def adjacentNumbers(x, y):
    numsAdjacent = 0
    gearRatio = 1
    if matGet(x-1, y, matrix).isdigit(): # left
        numsAdjacent+=1
        i = x-1
        num = ''
        while True:
            dig = matGet(i-1, y, matrix)
            if not dig.isdigit():
                break
            num = dig + num
            i-=1
        print(num)
        gearRatio*=int(num)
    if matGet(x+1, y, matrix).isdigit(): # right
        numsAdjacent+=1
    # directly above
    if matGet(x, y-1, matrix).isdigit():
        numsAdjacent+=1
    else: # if directly above isn't a digit, up left and up right could both be attached numbers
        if matGet(x-1, y-1, matrix).isdigit(): # up left
            numsAdjacent+=1
        if matGet(x+1, y-1, matrix).isdigit(): # up right
            numsAdjacent+=1
    # directly below
    if matGet(x, y+1, matrix).isdigit():
        numsAdjacent+=1
    else: # if directly above isn't a digit, down left and down right could both be attached numbers
        if matGet(x-1, y+1, matrix).isdigit(): # down left
            numsAdjacent+=1
        if matGet(x+1, y+1, matrix).isdigit(): # down right
            numsAdjacent+=1
    return numsAdjacent

for idx, line in enumerate(matrix):
    stars = findStars(line)
    for star in stars:
        numadj = adjacentNumbers(star, idx)
