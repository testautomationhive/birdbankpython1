import xlrd

def read_data():
    wb = xlrd.open_workbook("testdata/TestData.xls")
    sheet = wb.sheet_by_name("NewBiller")
    data = []
    for row in range(1, sheet.nrows):
        temp = []
        for col in range(sheet.ncols):
            temp.append(sheet.cell_value(row, col))
        data.append(temp)

    return data