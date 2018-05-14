import re
import requests
import json
import time
import pymysql

#pattern  = '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>'

def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
        pattern = re.compile(
            '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
            re.S
        )
        items = re.findall(pattern, html)
        #print(items)
        for item in items:
            yield {
                'index': item[0],
                'title': item[2].strip(),
                'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
                'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
                'score': item[5].strip() + item[6].strip()
            }
        #return item

def write_to_json(content):
    with open('movie.txt', 'a',encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def InsertData(TableName, dic):
        conn = pymysql.connect(host='localhost', user='root', passwd='wo@NI123', db='xxx', port=3306)
        SQL = ''
        try:
            with conn.cursor() as cursor:
                cursor.execute(SQL)
                conn.commit()
        except Exception as e:
            print(repr(e))

    # try:
    #     conn = pymysql.connect(host='localhost', user='root', passwd='wo@NI123', db='xxx', port=3306)  # 链接数据库
    #     cur = conn.cursor()
    #     COLstr = ''  # 列的字段
    #     ROWstr = ''  # 行字段
    #
    #     ColumnStyle = 'VARCHAR(20)'
    #     for key in dic.keys():
    #         COLstr = COLstr + ' ' + key + ColumnStyle + ','
    #         ROWstr = (ROWstr + '"%s"' + ',') % (dic[key])
    #
    #     #推断表是否存在，存在运行try。不存在运行except新建表，再insert
    #     try:
    #         cur.execute("SELECT * FROM  %s" % (TableName))
    #         cur.execute("INSERT INTO %s VALUES (%s)" % (TableName, ROWstr[:-1]))
    #
    #     except pymysql.Error:
    #         cur.execute("CREATE TABLE %s (%s)" % (TableName, COLstr[:-1]))
    #         cur.execute("INSERT INTO %s VALUES (%s)" % (TableName, ROWstr[:-1]))
    #     conn.commit()
    #     cur.close()
    #     conn.close()
    #
    # except pymysql.Error:
    #     print('error')

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_json(item)
        InsertData('movie', item)

if __name__ == '__main__':
    for i in range(10):
        main(offset= i * 10)
        time.sleep(1)
