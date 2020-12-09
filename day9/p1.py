def check(num, nums):
    for i in nums:
        for j in nums:
            if i!=j and i+j==num:
                return True
    return False

nums = []
with open('input.txt', 'r') as f:
   for i in f:
       nums.append(int(i))

for i in range(25, len(nums)):
    resp = check(nums[i], nums[i-25:i])
    if resp == False:
        print(nums[i])
        break