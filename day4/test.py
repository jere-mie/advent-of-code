# file I'm using to test my string checking

passports = "hgt:150cm            "
# checking eyr
index = passports.find("hgt:")+4
num = ""
height_line=""
for char in passports[index:]:
    if(char!=" " and char!='\n'):
        height_line+=char

if(len(height_line)>5 or len(height_line)<4):
    print('i1')
for char in height_line:
    if char.isdigit():
        num+=char
num = int(num)
if "cm" in height_line:
    if num>193 or num<150:
        print('icm')
elif "in" in height_line:
    if num>76 or num<59:
        print('iin')
else:
    print("i3")
