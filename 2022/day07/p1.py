inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    text = f.read().split("$ cd ")
sizes = dict()
text = list(filter(lambda x:x!='..\n', text))
text = [i.replace('$ ls\n', '') for i in text]
text = [i.split('\n') for i in text]
text = [list(filter(lambda x:x!='', i)) for i in text]
text = list(filter(lambda x: x!=[], text))
text.reverse()
for i in text:
    print(i)
    curr = 0
    for j in i[1:]:
        if j[:4] == 'dir ':
            curr+=sizes[j[4:]]
            print(f'{j[4:]} => {sizes[j[4:]]}')
        else:
            curr+=int(j.split(' ')[0])
    sizes[i[0]] = curr
# print(sizes['/'])
# print(sizes)
print(sum([sizes[i] if sizes[i]<=100000 else 0 for i in sizes]))
