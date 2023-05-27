import requests
import re
from datetime import datetime


class News():
    def __init__(self):
        self.string = ''
        # self.download()


    def download(self):
        f = open(file='最近一周发生的事件.txt', mode='w', encoding='utf8')
        url = 'https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/economy_zixun_1.jsonp?cb=economy_zixun'
        resp = requests.get(url=url)  # 用GET请求获取响应
        resp.encoding = 'utf-8'  # 设置编码格式
        webpage = resp.text  # 读取数据
        # 编写正则表达式
        s = r'"title":"(?P<title>.*?)","focus_date":"(?P<time>.*?)","url":"(?P<view_address>.*?)"'
        obj = re.compile(s, re.S)  # 用正则表达式创建抓取模板
        items = obj.finditer(webpage)  # 用模板获取一个带数据的迭代器
        i = 0
        for item in items:
            i = i + 1
            new_title = item.group('title')  # 通过group拿数据
            time = item.group('time')
            view_address = item.group('view_address')
            # print(time)
            if time[0:10] == datetime.today().strftime('%Y-%m-%d'):
                self.string += f'{i}：{new_title}\n发生时间：{time}\n浏览地址：{view_address}\n'
                f.write(f'{i}：{new_title}\n发生时间：{time}\n浏览地址：{view_address}\n')
        f.close()
        resp.close()
        return self.string


if __name__ == '__main__':
    # News().download()
    print(News().download())

