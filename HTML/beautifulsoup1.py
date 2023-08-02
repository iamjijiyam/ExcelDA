import bs4

webPage = open('Sample03.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

a_list = bsObject.findAll('a') #A에 대한 모든 값을 가져옴 
for aTag in a_list :
    print( aTag['href'] ) #a의 href 속성값들(URL)을 모두 출력함.

#따라서 URL 3개만 나오게 됩니다.
