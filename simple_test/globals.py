from manage_excel import readExcel
import os

CASE_NUMBER = 0
CASE_NAME = 1
CASE_METHOD = 2
CASE_URL = 3
CASE_DATA = 4
CASE_STATUS = 5
CASE_KEY = 6

cur_path = os.path.dirname(os.path.realpath(__file__))

file_path = cur_path + "\\test_case.xlsx"

host = "http://m.r7777.com.cn/v1.0.0/"

row_num = readExcel(file_path).getRows

class CASE:
    number = readExcel(file_path).getName(CASE_NAME)
    name = readExcel(file_path).getName(CASE_NAME)
    method = readExcel(file_path).getName(CASE_METHOD)
    url = readExcel(file_path).getName(CASE_URL)
    data = readExcel(file_path).getName(CASE_DATA)
    status = readExcel(file_path).getName(CASE_STATUS)
    key = readExcel(file_path).getName(CASE_KEY)