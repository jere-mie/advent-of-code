import re
lines = []
relats = dict()
with open('input.txt', 'r') as f:
    lines = f.readlines()
for i in lines:
    bag = re.findall(r'(\w+ \w+)(?: bags contain )', i)
    relats[bag[0]] = []
    if 'no' not in i:
        relats[bag[0]] = re.findall(r'(\d+) (\w+ \w+)', i)
def check(colour):
    sum=0
    for child in relats[colour]:
        sum+= int(child[0])+int(child[0])*check(child[1])
    return sum
print(check('shiny gold'))