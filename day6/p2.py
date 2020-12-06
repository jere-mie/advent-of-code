lines = []
with open('input.txt', 'r') as f:
    lines = f.read().split('\n\n')
total = 0
for i in lines:
    i = i.split('\n')
    temp = set(i[0])
    for j in i:
        temp2 = set(j)
        temp = temp&temp2
    total+=len(temp)
print(total)