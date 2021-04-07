import re
str1 = 'newdream'
str2 = '''hello123hello
hello123h
hello12h
hello1h
hello'''
#match从字符串开头开始匹配
# result = re.match('d\w+m',str1)
# print(result)

result = re.match('hello[\d,\D]+o',str2)
# print(result.group())

str3 = '''newdream come on!
newdream come good!
'''
# result_1 = re.match('(.+) (.+) (.+)',str3)
# print(result_1.group(3))
# print(result_1.group(1))
# print(result_1.group(1,3))

result_2 = re.match('(.+) come (.+)!',str3,re.I)
print(result_2.group())