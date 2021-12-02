import re
data = ''
with open('input.txt', 'r') as f:
    data = f.readlines()

depth = 0
horiz = 0
for i in data:
    num = int(re.findall(r'\d+', i)[0])
    if 'forward' in i:
        horiz+=num
    elif 'down' in i:
        depth+=num
    elif 'up' in i:
        depth-=num
    else:
        print('wut')
        exit()
print(f'h=>{horiz}, d=>{depth}, prod=>{horiz*depth}')