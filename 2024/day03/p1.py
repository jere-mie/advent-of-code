import re
inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().strip()
pattern = r'mul\((\d+),(\d+)\)'

tot = 0
matches = re.findall(pattern, text)
for match in matches:
    res = int(match[0]) * int(match[1])
    tot+=res
print(tot)
