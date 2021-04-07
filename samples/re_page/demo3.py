#seach 全字符串查找，找到第一个停止
import re
str = 'nEwDreamEaaaa'
pattern_01 = re.compile('Ea\w',re.IGNORECASE)
result_01 = re.search(pattern_01,str)
print(result_01.group())

result_02 = re.search('Ea\w',str,re.I)
print(result_02.group())
