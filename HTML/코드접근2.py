import bs4

webPage = open('Sample03.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag_div = bsObject.find('div') #div만 뽑아내는 조건 적용
print(tag_div)
