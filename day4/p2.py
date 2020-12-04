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
        # checking byr
        index = passports[j].find("byr:")+4
        year = int(passports[j][index:index+4])
        if !(pasports[j][index+4]==' ' or pasports[j][index+4]=='\n'):
            continue
        if !(year>=1920 and year<=2002):
            continue

        # checking iyr
        index = passports[j].find("iyr:")+4
        year = int(passports[j][index:index+4])
        if !(pasports[j][index+4]==' ' or pasports[j][index+4]=='\n'):
            continue
        if !(year>=2010 and year<=2020):
            continue
        
        # checking eyr
        index = passports[j].find("eyr:")+4
        year = int(passports[j][index:index+4])
        if !(pasports[j][index+4]==' ' or pasports[j][index+4]=='\n'):
            continue
        if !(year>=2020 and year<=2030):
            continue

        

print(valid)
print(len(passports))