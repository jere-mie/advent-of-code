inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    triangles = [[int(j) for j in i.split(' ')] for i in f.read().splitlines()]

valid_count = 0

for triangle in triangles:
    triangle.sort()
    if triangle[0] + triangle[1] > triangle[2]:
        valid_count += 1
print(valid_count)