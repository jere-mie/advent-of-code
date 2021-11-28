import re


msg = 'Hello World This is a String!'

words = re.findall(r'\w+', msg)
print(words)