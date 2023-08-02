import bs4

webPage = open('Sample02.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag_ul= bsObject.find('ul') #<ul>태그의 모든 내용을 추출함. 
print(tag_ul)               
print()

tag_ul= bsObject.find('li')  #<ul>태그의 하위 항목인 li,들을 찾음 
print(tag_li)
print()

tag_li_all= bsObject.findAll('li')
print(tag_li_all)