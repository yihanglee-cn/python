#coding=utf-8
import unittest
import requests
from logger import Log

url = 'http://ks.nice123.xin/v1.0.0/new/list'

class information(unittest.TestCase):
    '''资讯'''
    log = Log()

    def test_1_examInformation(self):
        '''考试资讯'''
        data = {'new_type':'0'}
        r = requests.post(url,data=data)
        exam_information = r.json()['data']['list'][1]['content']
        exam_sum = str(r.json()['data']['total'])
        self.assertEqual('这是考试资讯',exam_information)
        self.log.info(exam_information + "，共有" + exam_sum  + "条")

    def test_2_lessonsInformation(self):
        '''课程资讯'''
        data = {'new_type':'1'}
        r = requests.post(url,data=data)
        exam_information = r.json()['data']['list'][1]['content']
        exam_sum = str(r.json()['data']['total'])
        self.assertEqual('这是课程资讯',exam_information)
        self.log.info(exam_information + "，共有" + exam_sum  + "条")

    def test_3_allInformation(self):
        '''所有资讯'''
        data = {'new_type':''}
        r = requests.post(url,data=data)
        #exam_information = r.json()['data']['list'][1]['content']
        exam_sum = str(r.json()['data']['total'])
        #self.assertEqual('这是资讯',exam_information)
        self.log.info( "所有资讯，共有" + exam_sum  + "条")

if __name__ == "__main__":
    unittest.main()