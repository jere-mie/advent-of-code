lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

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
for j in range(len(passports)):
    if passports[j].find("byr")!=-1 \
    and passports[j].find("iyr")!=-1 \
    and passports[j].find("eyr")!=-1 \
    and passports[j].find("hgt")!=-1 \
    and passports[j].find("hcl")!=-1 \
    and passports[j].find("ecl")!=-1 \
    and passports[j].find("pid")!=-1:
        valid+=1
print(valid)
print(len(passports))