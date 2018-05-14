#-*- coding:utf-8 -*-
import unittest
import requests
from logger import Log

url = "http://ks.nice123.xin/v1.0.0/passport/login"
url_loginout = 'http://ks.nice123.xin/v1.0.0/passport/loginout'
login_token = 'test'

class Login(unittest.TestCase):
    log = Log()
    '''考试系统'''
    def test_1_login_pass(self):
        '''账号密码正确，登录成功'''
        data = {
            "account":"17688169411",
            "password":"lin123456"
        }
        r = requests.post(url,data=data)
        result = r.json()['data']['msg']
        self.assertEqual("登录成功",result)
        self.log.info("手机号为" + data["account"] + "的用户，" + result + '!')
        global login_token
        login_token = r.json()['data']['token']

    def test_2_loginout(self):
        '''token值正确，退出登录成功'''
        data = {
            "token":login_token,
        }
        r = requests.post(url_loginout,data=data)
        result = r.json()['data']['msg']
        self.assertEqual("退出成功",result)
        self.log.info("退出登录成功！")

    # def test_3_login_fail(self):
    #     '''账号为空，登录失败'''
    #     data = {
    #         "account":"",
    #         "password":"lin123456"
    #     }
    #     r = requests.post(url,data=data)
    #     result = r.json()['data']['msg']
    #     self.assertEqual("登录失败",result)
    #     self.log.info("登录失败，手机号不能为空！")

if __name__ == "__main__":
    unittest.main()