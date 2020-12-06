lines = []
with open('input.txt', 'r') as f:
    lines = f.read().split('\n\n')
total = 0
for i in lines:
    temp = set()
    for char in i:
        if char.isalpha():
            temp.add(char)
    total+=len(temp)
print(total)