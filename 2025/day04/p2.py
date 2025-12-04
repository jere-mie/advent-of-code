inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    grid = [list(i) for i in f.read().splitlines()]

def check_adjacent_rolls(grid, row, col):
    tot = 0
    if row > 0 and grid[row-1][col] == '@':
        tot += 1
    if row < len(grid)-1 and grid[row+1][col] == '@':
        tot += 1
    if col > 0 and grid[row][col-1] == '@':
        tot += 1
    if col < len(grid[0])-1 and grid[row][col+1] == '@':
        tot += 1
    if row > 0 and col > 0 and grid[row-1][col-1] == '@':
        tot += 1
    if row > 0 and col < len(grid[0])-1 and grid[row-1][col+1] == '@':
        tot += 1
    if row < len(grid)-1 and col > 0 and grid[row+1][col-1] == '@':
        tot += 1
    if row < len(grid)-1 and col < len(grid[0])-1 and grid[row+1][col+1] == '@':
        tot += 1
    return tot

total_rolls = 0

while True:
    coords_to_remove = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '@':
                if check_adjacent_rolls(grid, r, c) < 4:
                    coords_to_remove.add((r, c))
                    total_rolls += 1
    for r, c in coords_to_remove:
        grid[r][c] = '.'
    if not coords_to_remove:
        break

print(total_rolls)