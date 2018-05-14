#coding=utf-8
import unittest
import requests
from logger import Log

url = 'http://ks.nice123.xin/v1.0.0/index/list'

class HomePage(unittest.TestCase):
    log = Log()
    '''首页'''
    def test_1_GetHomePage(self):
        '''请求首页'''
        r = requests.post(url)
        global result
        result = r.json()
        self.log.info("首页请求成功！")

    def test_2_ExamList(self):
        '''转考直通车正确'''
        r = requests.post(url)
        result = r.json()
        exam_list_C = result['data']['examroom'][0]['title']
        self.assertEqual("C++",exam_list_C)
        self.log.info("首页存在" + exam_list_C + "考场！")

        exam_list_web = result['data']['examroom'][1]['title']
        self.assertEqual("web", exam_list_web)
        self.log.info("首页存在" + exam_list_web + "考场！")

        exam_list_PHP = result['data']['examroom'][2]['title']
        self.assertEqual("PHP", exam_list_PHP)
        self.log.info("首页存在" + exam_list_PHP + "考场！")

if __name__ == "__main__":
    unittest.main()