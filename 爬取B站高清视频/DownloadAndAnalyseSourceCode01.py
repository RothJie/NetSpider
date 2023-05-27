import time
import pyperclip
import pyautogui
import PIL       # 必须安装可以不用导入  pip install pillow
import cv2     # 必须安装可以不用导入 pip install python-opencv

"""
1.使用pyautogui通过浏览器获得网页源代码
2.解析源代码获得链接
"""

url = input('请输入链接：')

# 初始化pyautogui
pyautogui.PAUSE = 2  # 设置箭头大小为2
pyautogui.FAILSAFE = True  # 设置安全函数


def ToPngLocation(pn: str):  # 获取截图位置
    pos1 = pyautogui.locateCenterOnScreen(pn, confidence=0.8)
    pyautogui.moveTo(pos1)


pyautogui.hotkey('win', 'd')  # 退出界面

# 点击edg图标
ToPngLocation('01edg.png')
pyautogui.doubleClick()
time.sleep(2)

# 输入链接，进入网页源代码区域
pyperclip.copy(f'view-source:{url}')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')
time.sleep(1.5)

# 复制浏览器得到的网页源代码，并保存为文件WebSourcecode.html
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)
st_ = pyperclip.paste()  # 将剪贴板上的文本粘贴，并返回一个字符串类型的文本
# 将文件命名为WebSourcecode.html
with open(file=f'01_WebSourcecode.html', mode='w', encoding='utf-8') as f:
    f.write(st_)

# 点击退出浏览器
ToPngLocation('01exit.png')
pyautogui.click()

