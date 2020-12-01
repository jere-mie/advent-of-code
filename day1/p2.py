numbers = set()
with open("input.txt", "r") as f:
    for i in f:
        numbers.add(int(i))
for i in numbers:
    for j in numbers:
        if 2020-i-j in numbers:
            print(i*j*(2020-i-j))