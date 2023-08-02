import bs4

webPage = open('Sample03.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

print(bsObject)
#잠온다~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!
