
from bs4 import BeautifulSoup
import requests

name = input('Board:')
url = requests.get('https://www.ptt.cc/bbs/'+name)
url.encoding = 'utf-8'
soup = BeautifulSoup(url.text, 'lxml')
div = soup.find_all('div','r-ent')
for x in div:
    title = x.find('a')
    date = x.find('div', 'date')
    author = x.find('div', 'author')
    if title == None:
        pass
    else:
        print(name)
        print(date.string + title.string)
        print(author.string)
