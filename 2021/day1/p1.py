global data
with open('input.txt', 'r') as f:
    data = f.readlines()
data = [int(i) for i in data]
out = 0
for i in range(1, len(data)):
    if data[i] > data[i-1]:
        out+=1
print(out)