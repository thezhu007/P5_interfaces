import re

str1 = '137 5588 3666 ,#湖南号码'
str2 = str1.replace(' ','')
print(str2)

result_01 = re.sub('\s+','',str1)
print(result_01)
result_02 = re.sub('\d\s+\d','',str1)
print(result_02)
result_03 = re.sub('(\d+)\s+(\d+) (\d+)',r'1\2\3',str1)
print(result_03)
result_04 = re.sub('\s,.*$','',str1)
print(result_04)