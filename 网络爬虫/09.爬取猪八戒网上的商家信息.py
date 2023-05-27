import requests
from lxml import etree

pn = input("请输入你要检索的产品或服务信息：")
url = f'https://beijing.zbj.com/search/service?kw={pn}&r=2'

resp = requests.get(url)
resp.encoding = "utf-8"
# print(resp.text)
f = open(file=f'做{pn}的商家数据.csv', mode='w', encoding='utf8')
f.write(f'商家名称,所需价格,专注产品,评分,评论人数\n')

# 提起数据
et = etree.HTML(resp.text)
divs = et.xpath("//div[@class='search-result-list-service']/div")
for div in divs:
    # print(div)
    #  此时的数据，一个div对应一个商品信息
    price = div.xpath("./div/div/div[@class='price']/span/text()")
    if price == []:
        continue
    product_name = div.xpath("./div/div//a/text()")
    company_name = div.xpath("./div/a/div/div/div[@class='shop-info text-overflow-line']/text()")
    score = div.xpath("./div/div/div/div/span/span/text()")
    # score = div.xpath("./div/div[3]/div[4]/div[1]/span[1]/span/text()")
    num = div.xpath("./div/div[3]/div[4]/div[2]/span/div/span[2]/text()")
    print(company_name[0], price[0], product_name[0], score[0], num[0])
    f.write(f'{company_name[0]},{price[0]},{product_name[0]},{score[0]},{str(num[0])} \n')

resp.close()
f.close()
