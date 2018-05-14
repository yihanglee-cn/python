import xlrd
import xlwt
import os

filePath = os.path.dirname(os.path.realpath(__file__))

# 需求一：在当前路径下新建一个xlx表格，并在指定行写入数据

# 创建新工作簿
book = xlwt.Workbook(encoding='utf-8', style_compression=0)

# 添加一个sheet
sheet  = book.add_sheet('firstSheet', cell_overwrite_ok=True)

# 写数据
#sheet.write(0,0,'test')

data =[['24日（今天）', '多云', '【10℃~23°C】', '北风', '3-4级转<3级'],
       ['25日（明天）', '多云', '【11℃~25°C】', '西南风', '3-4级'],
       ['26日（后天）', '多云', '【13℃~26°C】', '西南风', '<3级转3-4级'],
       ['27日（周五）', '晴', '【14℃~26°C】', '西南风', '<3级转3-4级'],
       ['28日（周六）', '晴转多云', '【17℃~27°C】', '西南风', '3-4级转<3级'],
       ['29日（周日）', '多云转晴', '【17℃~28°C】', '东南风', '<3级'],
       ['30日（周一）', '多云', '【19℃~30°C】', '东南风', '3-4级']
       ]
for k,v in enumerate(data):
    for j,col in enumerate(v):
        sheet.write(k,j,col)

# 保存
book.save(filePath+'\\test.xls')