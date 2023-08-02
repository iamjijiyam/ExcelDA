import csv
import time
import datetime

csvName = 'D:\Python\DataExcel\ExcelDA\datetime.csv'
with open(csvName, 'w', newline='') as csvFp: #파일 열기(open), (W)를 통해 읽기 모드, 
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['연월일', '시분초']) #추출할 정보들

count = 10
while count > 0 :
    count -= 1

    now = datetime.datetime.now() #컴퓨터의 현재 시각 값을 가져옴
    yymmdd = now.strftime('%Y-%m-%d')
    hhmmss = now.strftime('%H:%M:%S')
    time_list = [yymmdd, hhmmss] #년 - 월 - 일 , 시 - 분 - 초
    print(time_list) #출력

    with open(csvName, 'a', newline='') as csvFp: #csv파일을 생성해서 기록 저장
            csvWriter = csv.writer(csvFp)
            csvWriter.writerow(time_list) 

    time.sleep(3) #3초 쉬기