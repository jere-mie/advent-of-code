with open('input.txt', 'r') as f:
    temp = list(map(int, f.read().strip().split(',')))
fish = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
for i in temp:
    fish[i]+=1

for i in range(80):
    temp = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for key in fish:
        if key==0:
            temp[6]+=fish[key]
            temp[8]+=fish[key]
        else:
            temp[key-1]+=fish[key]
    fish = temp

tot = 0
for i in fish:
    tot+=fish[i]
print(tot)