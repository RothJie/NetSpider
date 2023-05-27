import re
import time
import pyperclip
import pyautogui

"""
1.打开链接存放地址
2.解析获得名称 视频和音频下载链接
3.进入浏览器下载视频音频
"""


def Get_url():
    with open("./01_WebSourcecode.html", mode='r', encoding='utf-8') as f:  # 打开文件
        sourceCode = f.read()
    # 编写正则表达式
    for i in [64, 32]:
        video_str_ = f'>*?"id":{i},"baseUrl":"(?P<video_url>.*?)"'
        try:
            obj = re.compile(video_str_, re.S)
            video_url = obj.search(sourceCode).groups('video_url')[0]
        except AttributeError:
            continue


    for j in [30280, 30216]:
        audio_str_ = f'>*?"id":{j},"baseUrl":"(?P<audio_url>.*?)"'
        try:
            obj_ = re.compile(audio_str_, re.S)
            audio_url = obj_.search(sourceCode).groups('audio_url')[0]
        except AttributeError:
            continue

    name_str = '.*?id="viewbox_report".*?<h1 title="(?P<name_url>.*?)"'

    obj__ = re.compile(name_str, re.S)
    name = obj__.search(sourceCode).groups('name_url')[0]
    return name, video_url, audio_url


def ToPngLocation(pn: str):  # 获取截图位置
    pos1 = pyautogui.locateCenterOnScreen(pn, confidence=0.8)
    pyautogui.moveTo(pos1)


# 进入浏览器下载视频音频
def DownloadSource(sourceUrl: str):
    # 初始化pyautogui
    pyautogui.PAUSE = 2  # 设置箭头大小为2
    pyautogui.FAILSAFE = True  # 设置安全函数
    pyautogui.hotkey('win', 'd')  # 退出界面
    # 点击edg图标
    ToPngLocation('01edg.png')
    pyautogui.doubleClick()
    time.sleep(2)
    # 输入链接并下载资源
    pyperclip.copy(sourceUrl)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    time.sleep(60)
    # 点击退出浏览器
    ToPngLocation('01exit.png')
    pyautogui.click()


name, video_url, audio_url = Get_url()
print(f'{name}\n{video_url}\n\n{audio_url}')
DownloadSource(video_url)
DownloadSource(audio_url)


