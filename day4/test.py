# file I'm using to test my string checking

passports = "hcl:150abc            "
# checking eyr
# checking hcl
index = passports.find("hcl:")+4
colour = passports[index:index+7]
if not(passports[index+7]==' ' or passports[index+7]=='\n'):
    print('i1')
letters = 0
numbers = 0
for char in colour:
    if char.isdigit():
        numbers+=1
    if char >= 'a' and char<='f':
        letters+=1
if letters!=3 or numbers!=3 or colour[0]!='#':
    print('i2')
