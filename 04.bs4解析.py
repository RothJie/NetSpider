from bs4 import BeautifulSoup

html = """
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <meta content="always" <a href="//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg">图片</a> name="referrer">
    <meta content="always" <a href="//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg">图片</a> name="小李子">
    <meta name="theme-color" content="#ffffff">
    <li rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
    <li id="icon"><a href="//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg">图片</a>/li>
    <link rel="search" type="application/opensearchdescription+xml" href="/content-search.xml" title="百度搜索" />
            <link rel="apple-touch-icon-precomposed" href="https://psstatic.cdn.bcebos.com/video/wiseindex/aa6
            eef91f8b5b1a33b454c401_1660835115000.png">
"""

# 1.初始化BeautifulSoup对象
page = BeautifulSoup(html, "html.parser")

# 方法一.find（）
page.find("标签名", attrs={"属性", "值"})  # 查找某个元素
meta = page.find("meta", attrs={"content": "always"})

link = page.find("li", attrs={"id": "icon"})
a = link.find()
# print(a.text)  # 得到文本
# print(a.get("href"))  # 那特定属性中的值

# 方法二.findall（）
page.find_all("标签名", attrs={"属性", "值"})  # 查找一类标签, 返回一个列表
meta1 = page.find_all("meta", attrs={"content": "always"})
for i in meta1:
    t = i.text
    href = i.get("href")
    print(href)
    