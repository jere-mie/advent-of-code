text = open('input.txt', 'r').read().split('\n')
print(sum(map(lambda x: ord(x)-96 if x >= 'a' and x <= 'z' else ord(x)-38, [list(set(text[i]).intersection(set(text[i+1])).intersection(set(text[i+2])))[0] for i in range(0, len(text), 3)])))
