inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    lines = f.read().splitlines()

buttons = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

pos = [1, 1]
code = ''

for line in lines:
    for move in line:
        if move == 'U' and pos[0] > 0:
            pos[0] -= 1
        elif move == 'D' and pos[0] < 2:
            pos[0] += 1
        elif move == 'L' and pos[1] > 0:
            pos[1] -= 1
        elif move == 'R' and pos[1] < 2:
            pos[1] += 1
    code += str(buttons[pos[0]][pos[1]])
print(code)
