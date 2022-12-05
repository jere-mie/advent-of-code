import re
with open('input.txt', 'r') as f:
    data = f.read().split('\n\n')

# creating the list of cards
numbers = list(map(int, data[0].split(',')))
# print(numbers)

cards = []
for i in range(len(data[1:])):
    newcard = [list(map(int, re.findall(f'\d+', j))) for j in data[i+1].splitlines()]
    cards.append(newcard)
    # print(newcard)

def checkCol(card, col, called):
    for i in range(len(card)):
        if card[i][col] not in called:
            return False
    return True

def checkRow(card, row, called):
    for i in range(len(card[row])):
        if card[row][i] not in called:
            return False
    return True
# print(checkRow(cards[0], 0, [22, 13, 17, 11, 0]))
# print(checkRow(cards[0], 0, [21, 13, 17, 11, 0]))


def checkWinner(card, called):
    for i in range(len(card)): # checking all rows
        if checkRow(card, i, called):
            return True
    for i in range(len(card[0])): # checking all columns
        if checkCol(card, i, called):
            return True
    return False
# print(checkWinner(cards[0], [22, 13, 17, 11, 0]))
# print(checkWinner(cards[0], [21, 13, 17, 11, 0]))

calledNums = set()
winNum = -1
score = 0
# find winner
for num in numbers:
    calledNums.add(num)
    if len(cards)>1:
        cards = list(filter(lambda x:not checkWinner(x, calledNums), cards))
    else:
        if checkWinner(cards[0], calledNums):
            winNum = num
            break

# calculating the final score

for i in cards[0]:
    for j in i:
        if j not in calledNums:
            score+=j
score*=winNum
print(score)

