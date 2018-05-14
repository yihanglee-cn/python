import re
import pymysql
import requests
from bs4 import BeautifulSoup
import os

class SearchWeather():
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ''(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        self.connection = pymysql.connect(host='localhost', user='root', password='wo@NI123', db='xxx', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

    def getcityCode(self, cityName):
        SQL = "SELECT cityCode FROM cityWeather"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(SQL)
                self.connection.commit()
                result = cursor.fetchone()
            return result['cityCode']
        except Exception as e:
            print(repr(e))

    def getWeather(self, cityCode, cityname):
        url = "http://www.weather.com.cn/weather/%s.shtml" % cityCode
        html = requests.get(url, headers=self.headers)
        html.encoding='utf-8'
        soup = BeautifulSoup(html.text, 'lxml')
        weather = "日期       天气   【温度】       风向风力\n"
        datas = []
        for item in soup.find("div", {'id': '7d'}).find('ul').find_all('li'):
            date, detail = item.find('h1').string, item.find_all('p')
            title = detail[0].string
            templow = detail[1].find("i").string
            temphigh = detail[1].find('span').string if detail[1].find('span') else ''
            wind, direction = detail[2].find('span')['title'], detail[2].find('i').string
            if temphigh == '':
                weather += '你好，     【%s】今天白天：【%s】,      温度：【%s】,     %s：【%s】\n'% (cityname,title,templow,wind,direction)
            else:
                weather +=(date + title + "【" + templow +  "~"+temphigh +'°C】' + wind + direction + "\n")

            data = [date, title, "【" + templow +  "~"+temphigh +'°C】', wind, direction]
            datas.append(data)
        print(datas)


        return weather #此处有大坑！！！！！  由于缩进关系，return没有与for并列，导致值返回了一天的天气！！！找了半天，头痛。

    def saveWeather(self, detail):
        filePath = os.path.dirname(os.path.realpath(__file__))
        fileName = os.path.join(filePath + "\\天气.xls")
        with open(fileName, 'a' ) as f:
            f.write('                             \n')
            f.write('---------华丽的分割线----------\n')
            for details in detail:
                f.write(details)

    def main(self,city):
        cityCode = self.getcityCode(city)
        detail = self.getWeather(cityCode, city)
        self.saveWeather(detail)
        print(detail)



if __name__ == "__main__":
    weather = SearchWeather()
    weather.main(city=input('请输入需要查询的城市名称：'))


