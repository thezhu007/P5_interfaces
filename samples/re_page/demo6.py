import re
str1 = '中国$韩国$泰国$西班牙'
print(str1.split('$'))

str2 = '中国1韩国2泰国3西班牙'
print(str2.split('1'))
#maxsplit  分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数
print(re.split('\d',str2,maxsplit=0, flags=0))


