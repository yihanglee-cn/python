import xlrd
import os

class ExcelUtil():
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)

        self.keys = self.table.row_values(0)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1

            for i in range(self.rowNum-1):
                s = {}
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                    r.append(s)
                    j+=1
                return r
if __name__ == "__main__":
    cur_path = os.path.dirname(os.path.realpath(__file__))
    filePath = os.path.join(cur_path, "test.xlsx")
    print(cur_path)
    sheetName = 'Sheet1'
    data = ExcelUtil(filePath,sheetName)
    print(data.dict_data())
