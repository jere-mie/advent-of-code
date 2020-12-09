def check(num, nums):
    inval = 217430975
    tot = 0
    for i in range(num, len(nums)):
        tot+=nums[i]
        if tot==inval:
            return [num, i]
        elif tot>inval:
            return False
    return False

nums = []
inval = 217430975
with open('input.txt', 'r') as f:
   for i in f:
       nums.append(int(i))

for i in range(len(nums)):
    resp = check(i, nums)
    if resp:
        newlist = nums[resp[0]:resp[1]+1]
        print(max(newlist)+min(newlist))
        break
