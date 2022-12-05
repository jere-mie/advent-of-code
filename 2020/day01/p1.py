numbers = set()
with open("input.txt", "r") as f:
    for i in f:
        numbers.add(int(i))
for i in numbers:
    if 2020-i in numbers:
        print(i*(2020-i))