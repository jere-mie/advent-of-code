inpFile = 'input.txt'
with open(inpFile, 'r') as f:
    reports = [list(map(int, i.split())) for i in f.read().splitlines()]

numsafe = 0

def check_report(report):
    safe = 1
    sign = -1 if report[0]-report[1] < 0 else 1
    for i in range(len(report)-1):
        if abs(report[i]-report[i+1]) not in [1, 2, 3]:
            safe = 0
            break
        if (report[i]-report[i+1])*sign < 0:
            safe = 0
            break
    return safe > 0

def check_subreports(report):
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        safe = check_report(new_report)
        if safe:
            return True
    return False

for report in reports:
    if check_report(report):
        numsafe+=1
    elif check_subreports(report):
        numsafe+=1
print(numsafe)
