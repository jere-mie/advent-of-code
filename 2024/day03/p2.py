import re
DO = 2
DONT = 3
inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().strip()
pattern = r"(?:mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))"

tot = 0
matches = re.findall(pattern, text)
enabled = True
for match in matches:
    if match[DO]:
        enabled = True
    elif match[DONT]:
        enabled = False
    elif enabled:
        res = int(match[0]) * int(match[1])
        tot+=res
print(tot)
