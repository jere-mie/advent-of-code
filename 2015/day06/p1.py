import re
inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().splitlines()
    text = [list(re.search(f'(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)', i).groups()) for i in text]
    text = [i[:1]+list(map(int, i[1:])) for i in text]

lights = [[0 for i in range(1000)] for i in range(1000)]

def process(instruction, x1, y1, x2, y2):
    global lights
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if instruction == 'toggle':
                lights[i][j] = 1 if lights[i][j] == 0 else 0
            elif instruction == 'turn off':
                lights[i][j] = 0
            elif instruction == 'turn on':
                lights[i][j] = 1
for i in text:
    process(*i)
print(sum([sum(i) for i in lights]))