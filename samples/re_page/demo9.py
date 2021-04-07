import re
import requests

header_info = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}
response = requests.get(url='https://www.baidu.com/s?wd=云班课',
                        headers = header_info)
body_str = response.text

titls = re.findall( '"title":"(.+?)","url"' ,body_str)
print( titls )

contents = re.findall( 'opr-toplist1-subtitle">\s+(.+?)\s+</ a>[\s\S]+?([4-9][0-9][0-9]万?)</td>',body_str )
print( contents )