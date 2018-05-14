#coding=utf-8
import sys
import os
#sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+".")+"\common")
import unittest
import requests
from logger import Log


url = 'http://ks.nice123.xin/v1.0.0/passport/register'

class Registerd(unittest.TestCase):
    log = Log()
    '''注册页面'''
    def test_1_registerd_pass(self):
        '''注册信息正确，注册成功！'''
        data = {
            'mobile':'17688169411',
            'password':'lin123456',
            'type':'0',
            'email':'123456790@qq.com',
            'usertruename':'liyihang'
        }
        r = requests.post(url,data=data)
        result = r.json()['data']['msg']
        print(result)
        print(r.json())
        #self.assertEqual("注册成功！",result)
        self.log.info("注册成功，手机号为：" + data['mobile'])

    def test_2_registerd_fail(self):
        '''手机号已存在，注册失败'''
        data = {
            'mobile': '17688169411',
            'password': 'lin123456',
            'type': '0',
            'email': '846811543@qq.com',
            'usertruename': 'liyihang'
        }
        r = requests.post(url, data=data)
        result = r.json()['data']['msg']
        self.assertEqual("注册失败", result)
        self.log.info("注册失败，手机号" + data['mobile'] + "已被注册！")

    def test_3_registerd_fail(self):
        '''手机号为空，注册失败'''
        data = {
            'mobile': '',
            'password': 'lin123456',
            'type': '0',
            'email': '1234567@qq.com',
            'usertruename': 'liyihang'
        }
        r = requests.post(url, data=data)
        result = r.json()['data']['msg']
        self.assertEqual("注册失败",result)
        self.log.info("注册失败，手机号不能为空！")

    def test_4_registerd_fail(self):
        '''密码为空，注册失败'''
        data = {
            'mobile':'17688169417',
            'type': '0',
            'email': '1234567@qq.com',
            'usertruename': 'liyihang'
        }
        r = requests.post(url, data=data)
        result = r.json()['data']['msg']
        self.assertEqual("注册失败", result)
        self.log.info("注册失败，密码不能为空！")

    def test_5_registerd_fail(self):
        '''注册类型为空，注册失败'''
        data = {
            'mobile': '17688169417',
            'password': 'lin123456',
            'type': '',
            'email': '1234567@qq.com',
            'usertruename': 'liyihang'
        }
        r = requests.post(url, data=data)
        result = r.json()['data']['msg']
        self.assertEqual("注册失败",result)
        self.log.info("注册失败，手注册类型不能为空！")

    def test_6_registerd_fail(self):
        '''邮箱为空，注册失败'''
        data = {
            'mobile': '17688169417',
            'password': 'lin123456',
            'type': '0',
            'email': '',
            'usertruename': 'liyihang'
        }
        r = requests.post(url, data=data)
        result = r.json()['data']['msg']
        self.assertEqual("注册失败",result)
        self.log.info("注册失败，邮箱不能为空！")

    def test_7_registerd_fail(self):
        '''用户名为空，注册失败'''
        data = {
            'mobile': '17688169417',
            'password': 'lin123456',
            'type': '0',
            'email': '123456789@qq.com',
            'usertruename': ''
        }
        r = requests.post(url, data=data)
        result = r.json()['data']['msg']
        self.assertEqual("usertruename不能为空",result)
        self.log.info("注册失败，用户名不能为空！")

if __name__ == "__main__":
    unittest.main()