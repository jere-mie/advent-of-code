import re
inpFile = 'input.txt'
pattern = r'(\d+)\[(\w+)\]'
names = []
with open(inpFile, 'r') as f:
    lines = [[i.split('-')[0:-1], re.search(pattern, i.split('-')[-1]).groups()] for i in f.read().splitlines()]
total = 0
for line in lines:
    name = line[0]
    sectorID = int(line[1][0])
    # caesar shift each letter by sectorID
    shift = sectorID % 26
    decryptedName = ''
    for part in name:
        decryptedPart = ''
        for letter in part:
            decryptedLetter = chr(((ord(letter) - ord('a') + shift) % 26) + ord('a'))
            decryptedPart += decryptedLetter
        decryptedName += decryptedPart + ' '
    names.append((decryptedName.strip(), sectorID))

for name, sectorID in names:
    if 'north' in name:
        print(f'Found north pole objects at sector ID: {sectorID}, name: "{name}"')
