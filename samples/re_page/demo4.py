#findall 查找所有
import re
str = 'hello 123 hello'
result_01 = re.search('\w+',str)
result_02 = re.findall('\w+',str)
print(result_01.group())
print(result_02)
pattern = re.compile('\w+')
result_03 = pattern.findall(str,pos=5,endpos=12)
print(result_03)
