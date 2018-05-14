#coding=utf-8
import unittest
import requests
from logger import Log

class userInfo(unittest.TestCase):
    log = Log()
    '''个人中心'''
    def setUp(self):
        self.base_url = 'http://ks.nice123.xin/v1.0.0/home/get'

    def test_1_getUserInfo(self):

        '''获取用户信息'''
        data = {'userid':1}
        r = requests.post(self.base_url,data=data)
        user_result = r.json()['data']['info']['username']
        self.assertEqual('liyihang',user_result)
        self.log.info("用户信息获取成功，当前用户为：" + user_result)

if __name__ == "__main__":
    unittest.main()