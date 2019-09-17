# coding:utf-8

import openpyxl

class WriteExcel(object):

    def __init__(self, filename):
        self.filename = filename
        self.wb = openpyxl.load_workbook(filename)
        self.ws = self.wb.active

    def writeExcel(self, row_n, col_n, value):
        self.ws.cell(row_n, col_n).value = value
        self.wb.save(self.filename)

if __name__ == '__main__':
    wt = WriteExcel("F:\\pythonPjo\\pythonPro\\pythonPro\\data\\login.xlsx")
    wt.writeExcel(3, 1, "急啊急啊")


