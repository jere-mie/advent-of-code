with open('input.txt', 'r') as f:
    data = f.readlines()

ones = [0 for i in range(12)]
print(ones)

for i in data:
    for j in range(12):
        if i[j]=='1':
            ones[j]+=1

outstr = ''
for i in range(12):
    if ones[i] > (1000-ones[i]):
        outstr+='1'
    else:
        outstr+='0'

outstr2 = ''
for i in outstr:
    if i=='0':
        outstr2+='1'
    else:
        outstr2+='0'

print(int(outstr, 2)) # 1565
print(int(outstr2, 2)) # 1565
print(int(outstr, 2)*int(outstr2, 2)) # 1565

# 011000011101
# 100111100010