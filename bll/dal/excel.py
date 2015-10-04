import xlrd

"""Open Excel File"""
def openExcileFile(path):
    open_workbook = xlrd.open_workbook(path)
    return open_workbook

"""Get Sheet"""

def getSheet(wb):
    open_worksheet = wb.sheet_by_index(0)
    return open_worksheet