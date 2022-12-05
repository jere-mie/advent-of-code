with open('input.txt', 'r') as f:
    data = f.readlines()

oxdat = [i.strip() for i in data]
# let's find oxygen first
for i in range(12): # each digit
    if len(oxdat) == 1:
        break
    ones = 0
    common = ''
    for j in oxdat: # find most common bit
        if j[i] == '1':
            ones+=1
    if ones >= (len(oxdat)-ones):
        common = '1'
    else:
        common = '0'
    # removing uncommon bit strings
    newlist = []
    for j in oxdat:
        if j[i] == common:
            newlist.append(j)
    oxdat = newlist
print(oxdat)


codat = [i.strip() for i in data]
# let's find co2 now
for i in range(12): # each digit
    if len(codat) == 1:
        break
    ones = 0
    common = ''
    for j in codat: # find most common bit
        if j[i] == '1':
            ones+=1
    if ones >= (len(codat)-ones):
        common = '1'
    else:
        common = '0'
    # removing uncommon bit strings
    newlist = []
    for j in codat:
        if j[i] != common:
            newlist.append(j)
    codat = newlist
print(codat)

print(int(oxdat[0], 2)*int(codat[0], 2))
