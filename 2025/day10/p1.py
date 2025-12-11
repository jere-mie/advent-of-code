import itertools
inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    data = [i.split(' ') for i in f.read().splitlines()]

processed_data = []
for i in data:
    a = list(filter(lambda x: x in '#.', i[0]))
    b = [list(filter(lambda x: x.isdigit(), list(j))) for j in i[1:-1]]
    b = [list(map(int, j)) for j in b]
    processed_data.append([a, b])


def yield_combinations(buttons, depth):
    for i in itertools.product(buttons, repeat=depth):
        yield i

tot = 0

for datum in processed_data:
    lights = datum[0]
    buttons = datum[1]
    done = False
    depth = 1
    while depth <= 9 and not done:
        for combo in yield_combinations(buttons, depth):
            lights_copy = ['.' for i in lights]
            for button in combo:
                for light in button:
                    lights_copy[light] = '#' if lights_copy[light]=='.' else '.'
            if lights_copy == lights:
                tot += depth
                done = True
                break
        depth += 1
print(tot)
