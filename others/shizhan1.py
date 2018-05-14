#coding=utf-8
from selenium import webdriver
import unittest,time,re
import HTMLTestRunner
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class BaiDu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True
#搜索用例
    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)
if __name__ == "__main__":
    testunit=unittest.TestSuite()
    testunit.addTest(BaiDu("test_baidu_search"))
    filename = r'D:\python\result.html'
    #filename = '1.txt'
    print 1
    fp = file(filename,'wb')


    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,title=u'百度搜索测试报告',
        description=u'用例执行情况：')
    runner.run(testunit)