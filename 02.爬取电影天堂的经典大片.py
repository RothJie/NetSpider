"""
1.获取到主页面的每部电影的url
    1.获取主页面的网页源代码
    2.编写正则表达式，获取数据
2.拼接子页面的url,获取数据
"""
import requests
import re

f = open(file='电影天堂必看电影下载链接.csv', mode='w', encoding='utf8')
f.write(f'电影名称,下载地址\n')

url = 'https://www.dy2018.com'
resp = requests.get(url=url)
resp.encoding = 'gbk'
webpage = resp.text
# print(webpage)

# 编写正则表达式
str1 = r"经典大片</span>.*?<ul>(?P<data>.*?)</ul>"   # .*?  (?P<data>.*?)
str2 = r'<li><a href=(?P<url>.*?) title="(?P<movie>.*?)">'
str3 = r'<div id="Zoom">.*?<ul>		<li><a href="(?P<download>.*?)">'

obj1 = re.compile(str1, re.S)
result1 = obj1.search(webpage).group('data')
# print(result1)
obj2 = re.compile(str2, re.S)
items = obj2.finditer(result1)
for item in items:
    child_url = item.group('url')
    movie = item.group('movie')
    url3 = url.strip('/') + child_url.strip('\'')
    resp3 = requests.get(url3)
    resp3.encoding = 'gbk'
    webpage3 = resp3.text
    obj3 = re.compile(str3, re.S)
    download = obj3.search(webpage3).group('download')
    f.write(f'{movie},{download}\n')
    resp3.close()

f.close()
resp.close()
