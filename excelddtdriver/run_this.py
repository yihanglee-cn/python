# coding=utf-8
import unittest
import time
#from excelddtdriver.common import HTMLTestRunner_api
from BeautifulReport import BeautifulReport as bf
import os
# 1.获取当前文件夹路径
curpath = os.path.dirname(os.path.realpath(__file__))

# 2.定义报告存放路径
report_path = os.path.join(curpath, "report")

# 3.如果报告文件夹不存在就创建
if not os.path.exists(report_path): os.mkdir(report_path)

# 4.用例文件夹路径
case_path = os.path.join(curpath, "case")

def add_case(casepath=case_path, rule="test*.py"):
    '''加载所有的测试用例'''
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(casepath,pattern=rule,)

    return discover

def run_case(all_case, reportpath=report_path):
    '''执行所有的用例, 并把结果写入测试报告'''
    reportName = "接口测试报告.html"
    runner = bf(all_case)
    runner.report(description="接口测试", filename=reportName, log_path=report_path)

if __name__ == "__main__":
    cases = add_case()
    run_case(cases)

