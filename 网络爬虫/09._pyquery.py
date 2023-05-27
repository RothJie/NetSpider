from pyquery import PyQuery

html = """
    <ul>
        <li class="aaa"><a href="https://www.baidu.com">百度</a></li>
        <li class="aaa"><a href="https://www.google.com">谷歌</a></li>
        <li class="bbb" id="qq"><a href="https://www.tencent.com">腾讯</a></li>
        <li class="ccc"><a href="https://www.shuwu.com">书屋</a></li>
    </ul>
"""

# 加载html内容
pl = PyQuery(html)  # 通过选择器拿到类容
# a = pl(".aaa a")  # class="bbb"  通过类选择器提取
a = pl("#qq a")  # 通过ID选择器提取

a_attr = pl("#qq a").attr("href")  # 通过ID选择器提取，提取到属性值
a_text = pl("#qq a").text()  # 通过ID选择器提取，提取到文本
# print(a)
# print(a_attr)
# print(a_text)

# 多个标签拿属性
it = pl("li a").items()  # 先生成一个迭代器
for item in it:
    href = item.attr("href")  # 拿属性
    text = item.text()  # 拿文本

    # print(href, text)



div = """
    <div><span>你还好吗？</span></div>
"""
p = PyQuery(div)
html = p("div").html()  # 全部获取（HTML和文本）
text = p("div").text()  # 只要文本，所有的HTML标签都会被过滤掉
# print(html, text)



# 在XXXX标签后面添加XXXX新标签
# pl("li.ccc").after("""<li class="ccc"><a href="https://www.weimei.com">唯美</a></li>""")
# pl("li.ccc").append("""<li class="ccc"><a href="https://www.weimei.com">唯美</a></li>""")
pl("li.ccc").attr("class", "ddd")   # 修改属性
# pl("li.ccc").attr("id", "123456")  # 新增属性 前提是该标签没有这个属性
pl("li.bbb").remove_attr("id")  # 删除属性
pl("li.aaa").remove()  # 删除标签
# print(pl)
