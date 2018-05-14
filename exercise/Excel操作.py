import xlrd

# 打开表格
file = xlrd.open_workbook('test.xls')

table1 = file.sheets()[0]    #通过索引顺序获取
table2 = file.sheet_by_index(0)
table3 = file.sheet_by_name('Sheet1')
print(table1, table2, table3)

# 行数
nrows = table3.nrows
print(nrows)

# 列数
ncols = table3.ncols
print(ncols)

# 获取第一行值
print(table3.row_values(0))
print(table3.col_values(0))