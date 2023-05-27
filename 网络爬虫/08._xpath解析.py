from lxml import etree


html = ''
et = etree.HTML(html)
# li_list = et.xpath("/html/body/ul/li[2]/a/text()")
# print(li_list)

li_list = et.xpath("//li")  # 路径从li标签开始
for li in li_list:
    href = li.xpath("./a/@href")   # ./表示当前节点
    text = li.xpath("./a/text()")   # ./表示当前节点
    print(href, text)
