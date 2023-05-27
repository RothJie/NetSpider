# 1.拿到页面源代码
# 2.编写正则，拿到数据
# 3.保存数据
import re
import time
import requests

f = open(file='top250.csv', mode='w', encoding='utf8')
f.write(f'电影名称,导演,主演,年份,评分,评分人数\n')
for i in range(0, 251, 25):
    # 1.拿到页面源代码
    url = f'https://movie.douban.com/top250?start={i}&filter='

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }

    resp = requests.get(url=url, headers=headers)
    resp.encoding = 'utf-8'  # 解码
    pageSource = resp.text
    # print(pageSource)

    # 2.编写正则，拿到数据
    obj = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">'
                     r'.*?导演: (?P<daoyan>.*?)&nbsp;.*?主演: (?P<zhuyan>.*?)<br>(?P<year>.*?)&nbsp;.*?'
                     r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>',
                     re.S  # 可以使.匹配换行符
                     )
    result = obj.finditer(pageSource)
    for item in result:
        name = item.group('name')  # 拿结果
        daoyan = item.group('daoyan')  # 拿结果
        zhuyan = item.group('zhuyan')  # 拿结果
        year = item.group('year').strip()  # 拿结果
        score = item.group('score')  # 拿结果
        num = item.group('num')  # 拿结果
        f.write(f'{name},{daoyan},{zhuyan},{year},{score},{num}\n')
    resp.close()
    time.sleep(0.2)
f.close()
