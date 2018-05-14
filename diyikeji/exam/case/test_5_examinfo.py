#coding=utf-8
import unittest
import requests
from logger import Log

url = "http://ks.nice123.xin/v1.0.0/examroom/info"

class ExamInfo(unittest.TestCase):
    '''考场详情'''
    log = Log()

    def test_1_exam_PHP(self):
        '''PHP考场考场简介'''
        data = {'id':'1'}
        r = requests.post(url,data=data)
        exam_title = r.json()['data']['paper_info']['title']
        exam_description = r.json()['data']['paper_info']['description']
        self.assertEqual("本考场开启时间 不限 ； 考试次数 不限 ； 抽卷规则 用户手选试卷。",exam_description)
        self.log.info("进入" + exam_title + "考场成功！")

    def test_2_exam_web(self):
        '''web考场考场简介'''
        data = {'id':'2'}
        r = requests.post(url,data=data)
        exam_title = r.json()['data']['paper_info']['title']
        exam_description = r.json()['data']['paper_info']['description']
        self.assertEqual("本考场开启时间 不限 ； 考试次数 不限 ； 抽卷规则 用户手选试卷。",exam_description)
        self.log.info("进入" + exam_title + "考场成功！")

    def test_3_exam_C(self):
        '''C++考场考场简介'''
        data = {'id':'3'}
        r = requests.post(url,data=data)
        exam_title = r.json()['data']['paper_info']['title']
        exam_description = r.json()['data']['paper_info']['description']
        self.assertEqual("本考场开启时间 不限 ； 考试次数 不限 ； 抽卷规则 用户手选试卷。",exam_description)
        self.log.info("进入" + exam_title + "考场成功！")

if __name__ == "__main__":
    unittest.main()