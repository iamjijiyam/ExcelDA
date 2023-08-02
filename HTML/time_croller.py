import csv
import time
import datetime

csvName = 'D:\Python\DataExcel\ExcelDA\datetime.csv'
with open(csvName, 'w', newline='') as csvFp: #파일 열기(open), (W)를 통해 읽기 모드, 
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['연월일', '시분초']) #나는 도대체 왜 커밋오류가 뜨는지 모르겟다;;;;;;;;;;

count = 10 #알고보니 그냥 커밋메시지 안적고 커밋해서;;;;;;;
while count > 0 :
    count -= 1

    now = datetime.datetime.now() #컴퓨터의 현재 시각 값을 가져옴
    yymmdd = now.strftime('%Y-%m-%d')
    hhmmss = now.strftime('%H:%M:%S')
    time_list = [yymmdd, hhmmss] #년월일,시분초로 서식맞춤
    print(time_list) #출력

    with open(csvName, 'a', newline='') as csvFp: #csv파일을 생성해서 기록 저장
            csvWriter = csv.writer(csvFp)
            csvWriter.writerow(time_list) 

    time.sleep(3) #3초 쉬기