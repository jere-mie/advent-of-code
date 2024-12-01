inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    lines = f.read().splitlines()
left = []
right = []

for line in lines:
    nums = line.split("   ")
    left.append(int(nums[0]))
    right.append(int(nums[1]))

similarity = 0
rightcount = dict()
for i in right:
    rightcount[i] = rightcount.get(i, 0) + 1

for i in left:
    count = rightcount.get(i, 0)
    similarity += i*count
print(similarity)
