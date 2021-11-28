import re
lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
invalid = False
valid=0
temp=0
passports = []
passport = ""
for i in lines:
    if i =='\n':
        passports.append(passport)
        passport = ""
    else:
        passport+=str(i)
passports.append(passport)
for s in passports:
    print('byr')
    # matching byr
    match = re.search(r"(?<=byr:)\d{4}\b", s)
    if match==None:
        continue
    else:
        num = int(match.group())
        if not(num>=1920 and num<=2002):
            continue

    print('iyr')
    # matching iyr
    match = re.search(r"(?<=iyr:)\d{4}\b", s)
    if match==None:
        continue
    else:
        num = int(match.group())
        if not(num>=2010 and num<=2020):
            continue

    print('eyr')
    # matching eyr
    match = re.search(r"(?<=eyr:)\d{4}\b", s)
    if match==None:
        continue
    else:
        num = int(match.group())
        if not(num>=2020 and num<=2030):
            continue

    # matching pid
    print('pid')
    match = re.search(r"(?<=pid:)[0-9]{9}\b", s)
    if match==None:
        continue

    # matching ecl
    print('ecl')
    match = re.search(r"(?<=ecl:)(amb|blu|brn|gry|grn|hzl|oth)\b", s)
    if match==None:
        continue

    # matching hcl
    print('hcl')
    match = re.search(r"(?<=hcl:#)[0-9a-f]{6}\b", s)
    if match==None:
        continue

    # matching hgt
    print('hgt')
    match = re.search(r"(?<=hgt:)[0-9]+(in|cm)\b", s)
    if match==None:
        continue
    else:
        temp = match.group()
        num = int(temp[:-2])
        if "in" in temp:
            if num<59 or num>76:
                continue
        elif "cm" in temp:
            if num<150 or num>193:
                continue

    valid+=1

print(valid)
