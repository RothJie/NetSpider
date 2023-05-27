import requests
from bs4 import BeautifulSoup

url = "https://www.51miz.com/sucai/?tab=beijing"

resp = requests.get(url)
# resp.encoding = "utf-8"
main_page = BeautifulSoup(resp.text, "html.parser")
total_li = main_page.find_all("a", attrs={"class": "image-box"})

n = 0

for a in total_li:
    n += 1
    href = a.get("href")  # 拿到子页面网址
    resp_ = requests.get(url=href)
    resp_.encoding = "utf-8"
    # print(resp_.text)
    child_page = BeautifulSoup(resp_.text, "html.parser")
    url_P = child_page.find("div", attrs={"class": "img-box pa"})
    picture_url = "https:" + url_P.find("img").get("src")
    img_resp = requests.get(picture_url)
    with open(rf'C:\Users\Administrator\Pictures\Saved Pictures\新建文件夹\image{n}.jpg', mode='wb') as f:  # 以二进制的方式写入图片
        f.write(img_resp.content)  # 以二进制的方式写入图片用content

    resp_.close()
    img_resp.close()
    print(f"第{n}张图片下载完毕！！！！")

resp.close()
