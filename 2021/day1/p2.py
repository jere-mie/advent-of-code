global data
with open('input.txt', 'r') as f:
    data = f.readlines()
data = [int(i) for i in data]
out = 0
for i in range(3, len(data)):
    a,b,c,d = data[i-3:i+1]
    if (b+c+d)>(a+b+c):
        out+=1
print(out)