import re
str1 = 'newdream come on!!'
value = re.subn('(\w+) (\w+) (\w+)',r'\2 \3 \1',str1)
print(type(value))
print(value)
