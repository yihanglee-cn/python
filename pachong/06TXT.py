import requests
from pyquery import PyQuery as pq
import pymysql
import re

url = 'https://www.zhihu.com/explore'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5083.400 QQBrowser/10.0.972.400"
}
html = requests.get(url, headers=headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    dic = {
        'question': item.find('h2').text().format(),
        'author': item.find('.author-link-line').text().format(),
        'answer': pq(item.find('.content').html()).text().format()
    }
    print(dic)
    db = pymysql.connect(host='localhost', user='root', password='wo@NI123',
                         port=3306, db='alex')
    cursor = db.cursor()
    #create_table = 'CREATE TABLE IF NOT EXISTS zhihu(question VARCHAR(255) NOT NULL, author VARCHAR (255) NOT NULL, answer VARCHAR (5000) NOT NULL, PRIMARY KEY (question))'
    #cursor.execute(create_table)
    table = 'zhihu'
    keys = ','.join(dic.keys())
    values = ','.join(['%s'] * len(dic))
    #print(keys, values)
    insert_sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    cursor.execute(insert_sql, tuple(dic.values()))
    # try:
    #     if cursor.execute(insert_sql, tuple(dic.values())):
    #         print('ok')
    #         db.commit()
    # except:
    #     print('faild')
    #     db.rollback()
    db.close()