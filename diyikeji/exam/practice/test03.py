# coding:utf-8
from bs4 import BeautifulSoup
import requests
import os
r = requests.get("http://699pic.com/sousuo-218808-13-1.html")
fengjing = r.content
soup = BeautifulSoup(fengjing, "html.parser")
# 找出所有的标签
images = soup.find_all(class_="lazy")
# print images # 返回list对象
for i in images:
#    try:
        jpg_rl = i["data-original"]
        title = i["title"]
        print(title)
        print(jpg_rl)
        print("")
        with open(os.getcwd() + "\\jpg\\" + title + '.jpg', "wb") as f:
            f.write(requests.get(jpg_rl).content)
    # except:
    #     pass
