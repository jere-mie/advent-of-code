inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    reports = [list(map(int, i.split())) for i in f.read().splitlines()]

numsafe = 0
for report in reports:
    safe = 1
    sign = -1 if report[0]-report[1] < 0 else 1
    for i in range(len(report)-1):
        if abs(report[i]-report[i+1]) not in [1, 2, 3]:
            safe = 0
        if (report[i]-report[i+1])*sign < 0:
            safe = 0
    numsafe+=safe
print(numsafe)
