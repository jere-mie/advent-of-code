nums = []
nums.append(0)
heights = dict()
with open('input.txt', 'r') as f:
    for i in f:
        nums.append(int(i))
nums.sort()
nums.append(max(nums)+3)

def height(num, ind):
    tot = 0
    children = []
    cind = []
    if str(num) in heights:
        return heights[str(num)]
    else:
        for i in range(3):
            if ind+i+1<len(nums):
                if nums[ind+i+1]-num<=3:
                    children.append(nums[ind+i+1])
                    cind.append(ind+i+1)
        if len(children)==0:
            heights[str(num)] = 1
            return 1
        while children:
            tot+=height(max(children), max(cind))
            children.remove(max(children))
            cind.remove(max(cind))
        heights[str(num)] = tot
        return tot
print(height(nums[0], 0))