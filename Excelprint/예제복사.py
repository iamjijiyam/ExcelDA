import xlrd

workbook = xlrd.open_workbook('singer.xls')
sheetCount = workbook.nsheets
print('워크시트는 %d개 입니다' % (sheetCount))

wsheetList = workbook.sheets()
for worksheet in wsheetList :
    print('** 워크시트의 이름 : %s' % (worksheet.name) )
    print(" 행 수는 %d, 열 개수는 %d 입니다." % (worksheet.nrows, worksheet.ncols))

