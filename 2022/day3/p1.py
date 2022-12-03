inpfile = 'input.txt'

def convToInt(char):
    return ord(char)-96 if char >= 'a' and char <= 'z' else ord(char)-38

def splitAndIntersect(string):
    return convToInt(list(set(string[:int(len(string)/2)]).intersection(set(string[int(len(string)/2):])))[0])

with open(inpfile, 'r') as f:
    print(sum(map(lambda x:splitAndIntersect(x), f.read().split('\n'))))