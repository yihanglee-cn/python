import xlrd

class readExcel(object):
    def __init__(self, path):
        self.path = path
    @property
    def getSheet(self):
        #获取索引
        xl = xlrd.open_workbook(self.path)
        sheet = xl.sheet_by_index(0)
        return sheet

    def getRows(self):
        #获取行数
        rows = self.getSheet.nrows
        return rows
    @property
    def getCol(self):
        #获取列数
        col = self.getSheet.ncols
        return col

    #获取每一列的值
    def getName(self, colnum_index):
        if colnum_index <= self.getcol:
            ColumName = []
            for i in range(1, self.getRows):
                ColumName.append(self.getSheet.cell_value(i, colnum_index))
            return ColumName
        else:
            print("colnum不合法")

