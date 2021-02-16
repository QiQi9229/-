#-*- coding = utf-8 -*-
#@Time : 2021/2/15 20:18
#@Author : qiqi
#@File : 下载PPT模板.py
#@Software : PyCharm

# 批量下载视频
# https://qiubai-video.qiushibaike.com/2AY2PT2G9006WQRF_hd.mp4
# https://www.qiushibaike.com/video/
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68

import requests
from lxml import etree
import os

if not os.path.exists("./视频"):
    os.makedirs("./视频")

url = "https://www.qiushibaike.com/video/"
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68"
}
r = requests.get(url,headers=headers).text
# print(r)
html = etree.HTML(r)
j = 0
for i in range(1,3):
    if i == 1:
        url = "https://www.qiushibaike.com/video/"
    else:
        url = "https://www.qiushibaike.com/video/" + 'page/' + str(i) + '/'
    r1 = requests.get(url,headers=headers).text
    html1 = etree.HTML(r1)
    # 视频地址
    video = html1.xpath('//div[@class="col1 old-style-col1"]//source/@src')
    # print(video)

    for i in video:
        videourl = 'https:'+i
        # print(videourl)
        j+=1
        last_name = videourl.split('.')[-1]
        path = './视频/'+str(j)+'.'+last_name
        r2 = requests.get(videourl,headers=headers).content
        with open(path,'wb') as f:
            f.write(r2)
            print("第{}个视频下载完成".format(j))


