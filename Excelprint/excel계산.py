import xlrd

workbook = xlrd.open_workbook('singer.xls')
sheetCount = workbook.nsheets

personNum = 0
personIdx = 2
rowCount = 0
wsheetList = workbook.sheets()
for worksheet in wsheetList :
    rowCount += worksheet.nrows-1
    for row in range(1, worksheet.nrows) :
        personNum += int(worksheet.cell_value(row, personIdx))

print("전체 가수그룹 인원 합계 : ", personNum)
print("가수그룹 인원 평균 : ", personNum/rowCount)
