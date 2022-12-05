inpfile = 'input.txt'

with open(inpfile, 'r') as f:
    text = list(map(lambda x: x.split(' '), f.read().split('\n')))

outcomeScores = {'X':0, 'Y':3, 'Z':6}

def outcome(pair):
    Q, R = pair[0], pair[1]
    # rock
    if (Q=='A' and R=='Y') or (Q == 'B' and R == 'X') or (Q=='C' and R=='Z'):
        return 1+outcomeScores[R]
    # paper
    elif (Q=='A' and R=='Z') or (Q == 'B' and R == 'Y') or (Q=='C' and R=='X'):
        return 2+outcomeScores[R]
    # scissors
    else:
        return 3+outcomeScores[R]

score = sum(list(map(outcome, text)))
print(score)