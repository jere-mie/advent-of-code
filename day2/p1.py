import re
a = []
sum=0
with open('input.txt', 'r') as f:
    for i in f:
        a.append(i)
for i in a:
    temp = re.findall(r'\d+', i)
    nums = list(map(int, temp))
    index = i.find(':')
    letter = i[index-1:index]
    word = i[index+1:]
    tempsum = 0
    for char in word:
        if char==letter:
            tempsum+=1
    if tempsum>=nums[0] and tempsum<=nums[1]:
        sum+=1
print(sum)
