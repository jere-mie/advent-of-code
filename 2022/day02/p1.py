inpfile = 'input.txt'

with open(inpfile, 'r') as f:
    text = list(map(lambda x: x.split(' '), f.read().split('\n')))

shapeScores = {'X':1, 'Y':2, 'Z':3}

def outcome(pair):
    Q, R = pair[0], pair[1]
    # wins
    if (Q=='A' and R=='Y') or (Q == 'B' and R == 'Z') or (Q=='C' and R=='X'):
        return 6+shapeScores[R]
    # draws
    elif (Q=='A' and R=='X') or (Q == 'B' and R == 'Y') or (Q=='C' and R=='Z'):
        return 3+shapeScores[R]
    # losses
    else:
        return shapeScores[R]

score = sum(list(map(outcome, text)))
print(score)