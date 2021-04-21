import requests
from bs4 import BeautifulSoup


for i in range(1, 100, 10):
  url = 'https://search.naver.com/search.naver?&where=news&query=a&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=76&start={}&refresh_start=0'.format(i)
  response = requests.get(url)


  html = response.text
  soup = BeautifulSoup(html, 'html.parser')
  ul = soup.find('ul', attrs = {'class':'list_news'})
  # print(ul)

  content = ul.find_all('a', attrs = {'class': 'news_tit'})
  for a in content:
      print(a.text)
      print(a['href']) # 제목

  # print(ul.find_all('a'))