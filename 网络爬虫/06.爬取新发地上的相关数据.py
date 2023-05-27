import requests
import re
from bs4 import BeautifulSoup

url = "http://www.xinfadi.com.cn/getPriceData.html"

f = open(file='新发地数据.csv', mode='w', encoding='utf8')
f.write(f'id, name, low, high, avg, place\n')

rep = requests.get(url)
page = rep.text
# print(page)

rstr = r'.*?{"id":(?P<id>.*?),"prodName":"(?P<name>.*?)".*?' \
       r',"lowPrice":"(?P<low>.*?)","highPrice":"(?P<high>.*?)","avgPrice":"(?P<avg>.*?)","place":"(?P<place>.*?)'

obj = re.compile(rstr, re.S)
items = obj.finditer(page)
for item in items:
    id = item.group("id")
    name = item.group("name")
    low = item.group("low")
    high = item.group("high")
    avg = item.group("avg")
    place = item.group("place")
    f.write(f'{id},{name},{low},{high},{avg},{place}\n')

f.close()
rep.close()
