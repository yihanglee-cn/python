# import pymysql
#
# cityCodes = []
# connection = pymysql.connect(host='localhost', user='root', password='wo@NI123', db='xxx', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
# SQL = "SELECT cityCode FROM cityWeather"
# with connection.cursor() as cursor:
#     cursor.execute(SQL)
#     connection.commit()
#     result = cursor.fetchall()
#     print(result)
#
# # for i in result:
# #     for key, value in i.items():
# #         cityCodes.append(value)
# #         print(cityCodes)

import pymysql

db = pymysql.connect(host='localhost', user='root', password='wo@NI123',
                     port=3306, db='alex')
cursor = db.cursor()                 # 获取MySQL游标
# #cursor.execute('SELECT VERSION()')
# #data = cursor.fetchone()             # 获取执行SQL语句后的数据
# #print(data)
# #cursor.execute("CREATE DATABASE Alex DEFAULT CHARACTER SET utf8")
# sql = 'CREATE TABLE IF NOT EXISTS students(id VARCHAR(255) NOT NULL, name VARCHAR (255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)
# db.close()

# data = {
#     'id': '20180426',
#     'name': 'liyhang',
#     'age': '25'
# }
# table = 'students'
# # 用逗号分隔开data里面的key值，再拼接起来
# keys = ','.join(data.keys())
# # 定义长度为1的数组乘以列表的元素个数，再利用format方法构造表名，字段名，占位符
# values = ','.join(['%s'] * len(data))
# sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,
#                                                              keys=keys, values=values)
# try:
#     if cursor.execute(sql, tuple(data.values())):
#         print('ok')
#         db.commit()
# except:
#     print('faild')
#     db.rollback()
sql = 'SELECT * FROM students WHERE age >= 20'
try:
	cursor.execute(sql)
	print('Count:', cursor.rowcount)
	row = cursor.fetchone()
	while row:
		print('Row:', row)
		row = cursor.fetchone()
except:
	print('Error')
db.close()