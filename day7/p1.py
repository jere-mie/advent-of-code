def poppy(name, relats, name_stack, prev):
    for key in relats:
        if name in relats[key] and key not in prev:
            name_stack.append(key)

from os import name
import re
lines = []
relats = dict()
prev = set()
count = -1
name_stack = ['shiny gold']

with open('input.txt', 'r') as f:
    lines = f.readlines()
for i in lines:
    if "no" in i:
        continue
    bag = re.search(r'.+?(?= bags contain)', i).group()
    relats[bag] = []
    temp = re.search(r'(?<=contain \d )[\w ]+(?= bag)', i).group()
    relats[bag].append(temp)
    temp = re.findall(r'(?<=, \d )[\w ]+(?= bag)', i)
    for colour in temp:
        relats[bag].append(colour)

while name_stack:
    count +=1
    temp = name_stack.pop()
    prev.add(temp)
    poppy(temp, relats, name_stack, prev)

print(count)