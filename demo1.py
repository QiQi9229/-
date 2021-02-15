#-*- coding = utf-8 -*-
#@Time : 2021/2/15 16:10
#@Author : qiqi
#@File : demo1.py
#@Software : PyCharm

# 爬取京客隆网站店铺
# http://www.jkl.com.cn/cn/shop.aspx
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36
# http://www.jkl.com.cn/cn/shopLis.aspx?id=865


import requests
from lxml import etree
import pandas as pd

url = "http://www.jkl.com.cn/cn/shop.aspx"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
}


def Index(url):
    # 拿取每个城区网址
    r = requests.get(url,headers=headers).text
    # print(r)
    # 解析响应数据
    html = etree.HTML(r)

    # 获取每个城区店铺的id
    id = html.xpath('//div[@class="infoLis"]/ul/li/a/@href')
    # 拼接每个店铺的url
    base_url = "http://www.jkl.com.cn/cn/"
    for i in id:
        urls = base_url + i
        # 解析详情页
        Detail(urls)


def Detail(url):
    r = requests.get(url,headers=headers).text
    html = etree.HTML(r)
    # 店铺名称
    name = html.xpath('//span[@class="con01"]/text()')
    # 地址
    address = html.xpath('//span[@class="con02"]/text()')
    # 电话号码
    phone = html.xpath('//span[@class="con03"]/text()')
    # 营业时间
    time = html.xpath('//span[@class="con04"]/text()')
    list = [ ]
    for i in name:
        new_name = i.strip()
        list.append(new_name)

    # 写入数据到Excel
    Data = pd.DataFrame({"店名":list,"地址":address,"电话":phone,"营业时间":time})
    Data.to_csv('./店铺信息1.csv',index=False,header=0,mode='a',encoding="ANSI")
    

if __name__ == '__main__':
    Index(url)


