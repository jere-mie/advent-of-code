inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    grid = [list(i) for i in f.read().splitlines()]
split = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S' or grid[i][j] == '|':
            try:
                if grid[i+1][j] == '.':
                    grid[i+1][j] = '|'
                elif grid[i+1][j] == '^':
                    split += 1
                    grid[i+1][j-1] = '|'
                    grid[i+1][j+1] = '|'
            except IndexError:
                pass
print(split)