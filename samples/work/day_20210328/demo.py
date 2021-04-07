import requests,random,re


response = requests.get(url='http://47.107.178.45/phpwind/')
body_str = response.text
tids = re.findall('< a href=" " class="st" style="" title="(.+?)">(.+?)</ a>',body_str )
tid_list = []
for tid in tids:
    tid_list.append(tid[1])