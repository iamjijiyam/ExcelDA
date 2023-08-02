import xlrd

workbook = xlrd.open_workbook('singer.xls')
sheetCount = workbook.nsheets

wsheetList = workbook.sheets()
for worksheet in wsheetList : 
    print('** 워크시트의 이름 : %s' % (worksheet.name))
    for row in range(worksheet.nrows) : #데이터를 뽑아와서 행 열 
        for col in range(worksheet.ncols) :
         print ("%s" % worksheet.cell_value(row, col),end='\t')
    print()
print()         