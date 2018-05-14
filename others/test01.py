#coding=utf-8
import unittest
from selenium import webdriver

url = "http://47.91.209.159:802/"

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()

    def test_contanctUs(self):
        self.driver.find_element_by_xpath('//*[@id="nav83"]/a').click()

        try:
            self.driver.find_element_by_xpath('/html/body/div[5]/div/div[3]').is_displayed()
        except:
            print "跳转至联系我们界面失败"
        else:
            print "跳转至联系我们界面成功"

    #def test_firstPage(self):
        self.driver.find_element_by_xpath('//*[@id="nav1"]/a').click()

        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/a/img').is_displayed()
        except:
            print "跳转至首页失败"
        else:
            print "跳转至首页成功"

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
        unittest.main()


