import requests
from bs4 import BeautifulSoup

url = "https://sports.qq.com/"
r = requests.get(url)
print(r.encoding)
r.encoding = 'gbk'

# print(r.text)
soup = BeautifulSoup(r.text, 'lxml')
cnt = 0
# print(soup)
for news in soup.find_all('a'):  # , class_="item-txt"
    cnt += 1
    # info = news.find('a')
    # if info:
    link = str(news.get('href'))
    title = news.get_text()
    title.replace(" ", "")
    title.strip()
    if link != 'None' and title != 'None':
        print(f"链接：{link}")
        print(f"标题：{title}\n")
print(cnt)
