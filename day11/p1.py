seats = []
with open('input.txt', 'r') as f:
    seats = f.readlines()
for i in range(len(seats)):
    # if seats[i][-1]=='\n':
    #     seats[i] = list(seats[i][0:-1])
    # else:
    seats[i] = list(seats[i])
    if '\n' in seats[i]:
        seats[i].remove('\n')
def numadj(i, j):
    sum=0
    # checking top
    if i!=0:
        if seats[i-1][j]=='#': sum+=1
        if j!=0:
            if seats[i-1][j-1]=='#': sum+=1
        if j<len(seats[i])-1:
            if seats[i-1][j+1]=='#': sum+=1
    # checking bottom
    if i<len(seats)-1:
        if j!=0:
            if seats[i+1][j-1]=='#': sum+=1
        # print(f'i:{i}, j{j}')
        if seats[i+1][j]=='#': sum+=1
        if j<len(seats[i+1])-1:
            if seats[i+1][j+1]=='#': sum+=1

    # checking middle
    if j!=0:
        if seats[i][j-1]=='#': sum+=1
    if j<len(seats[i])-1:
        if seats[i][j+1]=='#': sum+=1

    return sum

def changeSeats():
    seats2 = [seat for seat in seats]
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if numadj(i, j)==0 and seats[i][j]=='L':
                seats2[i][j]='#'
            if numadj(i, j)>=4 and seats[i][j]=='#':
                seats2[i][j]='L'
    return seats2

newSeats = changeSeats()
while newSeats!=seats:
    seats = [seat for seat in newSeats]
    newSeats = changeSeats()

numO=0
for i in newSeats:
    for j in i:
        if j=='#':
            numO+=1

print(numO)