nums = []
diff3 = 0
diff1 = 0
nums.append(0)
with open('input.txt', 'r') as f:
    for i in f:
        nums.append(int(i))
nums.sort()
nums.append(max(nums)+3)
for i in range(len(nums)-1):
    diff = nums[i+1]-nums[i]
    if diff==3:
        diff3+=1
    elif diff==1:
        diff1+=1

print(diff1*diff3)