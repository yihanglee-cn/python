#coding=utf-8
'''
用例执行框架
执行所有用例
创建测试报告
'''
import unittest
import HTMLTestRunner
import os
import time
from BeautifulReport import BeautifulReport

#   获取当前所在文件的真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))
print("当前的路径是："+cur_path)

def add_case(caseName="case",rule="test*.py"):
    '''第一步 加载所有用例'''
    case_path = os.path.join(cur_path,caseName)
    if not os.path.exists(case_path):os.mkdir(case_path)
    print("case路径是："+case_path)
#   定义discover
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    #print(discover)
    return discover

def run_case(all_case,reportName="report"):
    '''第二步 执行所有用例'''
#   获取当前时间
    cur_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    #print(cur_time)
#   获取当前报告文件夹的路径，如果不存在就创建
    report_dir_path = os.path.join(cur_path,reportName)
    if not os.path.exists(report_dir_path):os.mkdir(report_dir_path)
    report_path = os.path.join(cur_time+"_result.html")
    #print("测试报告的路径是："+report_dir_path)

    #new_file = open(report_path,"wb")
    # runner = HTMLTestRunner.HTMLTestRunner(stream=new_file,
    #                                        title="考试系统测试报告",
    #                                        description="用例执行情况:")
    runner = BeautifulReport(all_case)
    runner.report(filename=report_path,description="hi",log_path=report_dir_path)
    #runner.run(all_case)
    #new_file.close()

if __name__ == "__main__":
    all_case = add_case()
    run_case(all_case)