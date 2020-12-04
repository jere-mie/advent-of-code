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
for j in range(len(passports)):
    if passports[j].find("byr")!=-1 \
    and passports[j].find("iyr")!=-1 \
    and passports[j].find("eyr")!=-1 \
    and passports[j].find("hgt")!=-1 \
    and passports[j].find("hcl")!=-1 \
    and passports[j].find("ecl")!=-1 \
    and passports[j].find("pid")!=-1:
        # checking byr
        print("byr")
        index = passports[j].find("byr:")+4
        year = int(passports[j][index:index+4])
        if not(passports[j][index+4]==' ' or passports[j][index+4]=='\n'):
            continue
        if not(year>=1920 and year<=2002):
            continue
        # checking iyr
        print("iyr")
        index = passports[j].find("iyr:")+4
        year = int(passports[j][index:index+4])
        if not(passports[j][index+4]==' ' or passports[j][index+4]=='\n'):
            continue
        if not(year>=2010 and year<=2020):
            continue
        
        # checking eyr
        print("eyr")
        index = passports[j].find("eyr:")+4
        year = int(passports[j][index:index+4])
        if not(passports[j][index+4]==' ' or passports[j][index+4]=='\n'):
            continue
        if not(year>=2020 and year<=2030):
            continue
        
        # checking pid
        print("pid")
        index = passports[j].find("pid:")+4
        num = passports[j][index:index+9]
        if not(passports[j][index+9]==' ' or passports[j][index+9]=='\n'):
            continue
        numbers=0
        for char in num:
            if char.isdigit():
                numbers+=1
        if not(numbers==9):
            continue

        # testing ecl
        print("ecl")
        index = passports[j].find("ecl:")+4
        color = passports[j][index:index+3]
        colors = ["amb","blu","brn","gry","hzl","oth"]
        if not(passports[j][index+3]==' ' or passports[j][index+3]=='\n'):
            continue
        if not(color in colors):
            continue

        # checking hgt
        print("hgt")
        index = passports[j].find("hgt:")+4
        num = ""
        height_line=""
        for char in passports[j][index:]:
            if(char!=" " and char!='\n'):
                height_line+=char

        if(len(height_line)>5 or len(height_line)<4):
            continue
        for char in height_line:
            if char.isdigit():
                num+=char
        num = int(num)
        if "cm" in height_line:
            if num>193 or num<150:
                continue
        elif "in" in height_line:
            if num>76 or num<59:
                continue
        else:
            continue

        # checking hcl
        print("hcl")
        index = passports[j].find("hcl:")+4
        colour = passports[j][index:index+6]
        if not(passports[j][index+6]==' ' or passports[j][index+6]=='\n'):
            continue
        letters = 0
        numbers = 0
        for char in colour:
            if char.isdigit():
                numbers+=1
            if char >= 'a' and char<='f':
                letters+=1
        if letters!=3 or numbers!=3:
            continue

        valid+=1

print(valid)
print(len(passports))