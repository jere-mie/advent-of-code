import sys
import os

# checking args
if(len(sys.argv) != 3):
    print("INCORRECT ARGUMENTS")
    print("Run like the following:")
    print("python3 new.py 2022 02")
    exit()

# checking arg format
year, day = sys.argv[1:]
if(len(year) != 4) or (len(day) != 2):
    print("INCORRECT ARGUMENTS")
    print("Run like the following:")
    print("python3 new.py 2022 02")
    exit()

# file creation and such
path = f'{year}/day{day}'
if os.path.exists(path):
    print("Day already exists")
    exit()
os.mkdir(path)
open(f'{path}/input.txt', 'w').close()
open(f'{path}/test.txt', 'w').close()
with open(f'{path}/p1.py', 'w') as f:    
    f.write("""inpFile = 'test.txt'
with open(inpFile, 'r') as f:
    text = f.read().splitlines()
print(text)
""")

print(year, day, "Created!")