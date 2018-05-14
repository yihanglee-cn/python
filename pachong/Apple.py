from requests_html import HTMLSession

url = "https://www.apple.com/hk-zh-hiEd/shop/browse/home/specialdeals/mac/macbook_pro/15"

session = HTMLSession()

r = session.get(url=url)

macPro = r.html.find('.box-content', first=True).text
print(macPro)
with open('apple.txt', 'a', encoding='utf-8') as f:
    f.write(macPro)

# import requests
# from pyquery import PyQuery as pq
#
#
# url = "https://www.apple.com/hk-zh-hiEd/shop/browse/home/specialdeals/mac/macbook_pro/15"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5083.400 QQBrowser/10.0.972.400"
# }
# html = requests.get(url=url, headers=headers).text
# doc = pq(html)
# items = doc(".box-content").items()
# for item in items:
#     dic = {
#         "product" : item.find('h3').text()
#     }
#     print(dic)
#     with open("apple.txt", 'a', encoding='utf-8') as f:
#         f.write(dic)

# 读取txt
