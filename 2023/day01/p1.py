import re

inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().splitlines()

digit_lists = [re.findall(r'\d', i) for i in text]
nums = [int(i[0]+i[-1]) for i in digit_lists]
print(sum(nums))
