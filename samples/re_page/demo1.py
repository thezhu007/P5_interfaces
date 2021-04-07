#正则表达式基础
import re
str1 = 'newdream'
str2 = '''hello123hello
hello123h
hello12h
hello1h
hello'''
#方式一：
pattern_1 = re.compile('n\w+m')
# print(pattern_1)
result_01 = re.match(pattern_1,str1)
print(result_01.group())

pattern_2 = re.compile('hello\d+h')
result_02 = re.findall(pattern_2,str2)
print(result_02)

#方式二：
result_03 = re.match('n\w+m',str1)
print(result_03.group())

#方式三：
result_04 = pattern_1.match(str1)
print(result_04.group())

