inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    lines = f.read().splitlines()
left = []
right = []

for line in lines:
    nums = line.split("   ")
    left.append(int(nums[0]))
    right.append(int(nums[1]))
left.sort()
right.sort()

distances = []
for i in range(len(left)):
    distances.append(abs(left[i]-right[i]))

print(sum(distances))
