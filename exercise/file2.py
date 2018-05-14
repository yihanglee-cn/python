#coding=utf-8

import csv

filepath = 'G:\\CodeByLyh\\exercise\\files\\test.csv'

with open(filepath, encoding='utf-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
