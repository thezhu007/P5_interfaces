#re.finditer 查找所有，并返回迭代器，迭代器中都是match对象

import re
str = 'hello 123 hello'
pattern = re.compile('\w+')
result_03 = pattern.finditer(str,pos=5,endpos=12)
print(type(result_03))
for i in result_03:
    print(i.group())