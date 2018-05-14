#coding=utf-8
import unittest
import os
import time
from BeautifulReport import BeautifulReport as BF

cur_path = os.path.dirname(os.path.realpath(__file__))  #获取当前文件的真实路径，dirname去掉文件名返回目录，realpath获取文件路径

def add_case(caseName="case",rule="test*.py"):  #加载所有测试用例
    case_path = os.path.join(cur_path,caseName) #用例路径，文件夹为case
    print("用例路径为：" + case_path)
    if not os.path.exists(case_path):os.mkdir(case_path)    #如果不存在case文件夹就创建
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)   #使用discover加载所有用例
    return discover

def run_case(all_case,reportName="report"):
    cur_time = time.strftime('%Y-%m-%d_%H%M%S')   #获取并格式化输出当前时间
    report_dir_path = os.path.join(cur_path,reportName) #定义报告路径
    print("测试报告路径为：" + report_dir_path)
    if not os.path.exists(report_dir_path):os.mkdir(report_dir_path)    #如果report文件夹不存在，就自动创建
    report_name = os.path.join(cur_time+"-测试报告.html")    #定义报告文件名称
    # 调用beautifulreport
    runner = BF(all_case) #调用失败的可能原因：BF模块丢到site-pakage里时出现多余的层级目录
    runner.report(filename=report_name,description="考试系统-接口测试",log_path=report_dir_path)

if __name__ == "__main__":
    all_case = add_case()
    run_case(all_case)
