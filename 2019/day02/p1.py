inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    nums = f.read().split(',')
    nums = [int(i) for i in nums]

nums[1] = 12
nums[2] = 2

i = 0
while i<len(nums):
    op = nums[i]
    if op == 99:
        print("Halting")
        break
    elif op == 1 or op == 2:
        nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]] if op == 1 else nums[nums[i+1]]*nums[nums[i+2]]
        i+=4
    else:
        print(f"Wtf??? Op = {op}")
        exit(1)
print(nums[0])
