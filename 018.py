import requests as r
from bs4 import BeautifulSoup
url = 'https://www.pracuj.pl/praca/python;kw?rd=0'
page = r.get(url)
soup = BeautifulSoup(page.content,'html.parser')
print(soup.title)
print(page.content)
element = soup.find('span',class_="results-header__offer-count-text-number")
print('We have',element.text,'offerts.')