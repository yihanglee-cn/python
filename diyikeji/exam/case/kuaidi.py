#coding=utf-8
#Author:liyihang
#Date:2018-02-27

import unittest
import requests

class Test_Kuaidi(unittest.TestCase):
    def setUp(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) "
                                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/52.0.2743.116 Safari/537.36"}

    def test_chaxun(self):
        '''查询快递（韵达）'''
        # danhao = "3903953369212"
        # kd = "yunda"
        self.url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-3903953369212-yunda.html"
        #print(self.url)
        # 第一步 发送请求
        r = requests.get(self.url,headers=self.headers,verify=False)
        result = r.json()
        print(result)
        # 第二步 获取结果
        # 获取快递公司名称
        #print(result['company'])
        # 获取data里的内容
        data = result["data"]
        # 列表里第一个
        #print(data[0])
        #列表中的第一个值是一个字典，取字典中的值
        get_result = data[0]['context']
        #print(get_result)
        # 断言
        self.assertIn(u"已签收",get_result)
        print("成功！")

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()