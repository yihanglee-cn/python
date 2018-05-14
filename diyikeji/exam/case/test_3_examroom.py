#coding=utf-8
import unittest
import requests
from logger import Log

url = "http://ks.nice123.xin/v1.0.0/examroom/info"

class ExamRoom(unittest.TestCase):
    log = Log()
    '''选择考场'''
    def test_1_PHP(self):
        '''当id=1时，进入PHP考场'''
        data = {'id':'1'}
        r = requests.post(url,data=data)
        exam_title = r.json()['data']['paper_info']['title']
        self.assertEqual("PHP", exam_title)
        self.log.info("进入"+exam_title+"考场成功!")

    def test_2_web(self):
        '''当id=2时，进入web考场'''
        data = {'id':'2'}
        r = requests.post(url,data=data)
        exam_title = r.json()['data']['paper_info']['title']
        self.assertEqual("web", exam_title)
        self.log.info("进入" + exam_title + "考场成功!")

    def test_3_C(self):
        '''当id=3时，进入C++考场'''
        data = {'id':'3'}
        r = requests.post(url,data=data)
        exam_title = r.json()['data']['paper_info']['title']
        self.assertEqual("C++", exam_title)
        self.log.info("进入" + exam_title + "考场成功!")

if __name__ == "__main__":
    unittest.main()