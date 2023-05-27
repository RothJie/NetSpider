"""
1.进入文件存储地址
2.把最新下载的两个文件合并为视频文件
2.1最后下载的是音频重命名为audio.mp3
2.1下面是视频重命名为video.mp4
2.3用命令合并为name.mp4 并保存到指定位置
"""
import os
import time
import subprocess
import Download_videoAndaudio02

files = os.listdir(r'C:\Users\Administrator\Downloads')


def Rename():
    os.rename(rf'C:\Users\Administrator\Downloads\{files[0]}', fr"C:\Users\Administrator\Downloads\video.mp4")
    os.rename(rf'C:\Users\Administrator\Downloads\{files[1]}', fr"C:\Users\Administrator\Downloads\audio.mp3")


name, a, b = Download_videoAndaudio02.Get_url()
# name = "第二个"


def MergeSource():
    print("视频合成中。。。。。。。。。。")
    cmd = fr'ffmpeg -i C:\Users\Administrator\Downloads\video.mp4 -i C:\Users\Administrator\Downloads\audio.mp3 -acodec copy -vcodec copy G:\B站高清视频\{name[:22]}.mp4'
    subprocess.call(cmd, shell=True)
    time.sleep(5)
    if os.path.exists(rf'G:\B站高清视频\{name[:22]}.mp4'):
        os.remove(r"C:\Users\Administrator\Downloads\video.mp4")
        os.remove(r"C:\Users\Administrator\Downloads\audio.mp3")
        print(f"{name[:22]}.mp4   视频已经下载完成了。。。。")
    else:
        print("视频无法合成！！！！")


Rename()
MergeSource()
for i in range(5):
    time.sleep(2)
    print('视频处理完毕，10秒 后自动退出！')
