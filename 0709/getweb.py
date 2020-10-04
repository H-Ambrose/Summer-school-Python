import requests
from bs4 import BeautifulSoup

url = "https://tech.163.com/"
print(f"网页地址: {url}\n")
r = requests.get(url)
# print(r.encoding) 检查encoding类型
r.encoding = 'gb2312'

soup = BeautifulSoup(r.text, 'lxml')
cnt = 0
all_class = set()
for news in soup.find_all('a'):  # class_ = newest_lists
    # 为了能够爬取更多新闻, 这里没有使用find_all('li')
    link = str(news.get('href'))
    cla = str(news.get('class'))
    text = news.find('p')

    if text:  # 如果没有这部分，会把一些其他链接包括进来
        if cla == 'None':
            cla = str(text.get('class'))
        if cla == 'None':
            cla = news.find('div')
            if cla:
                cla = str(cla.get('class'))
        title = str(text.get_text())
        # title = title.replace(" ", "") 去掉空格
        pos = title.find(':')
        if pos != -1 and title[pos-1].isdigit():  # 网页内容中包含时间
            title = title.strip()[:-5].strip()
        title = title.strip()
        if link != '' and title != '':
            cnt += 1
            all_class.add(cla)
            print(f"类型: {cla}")
            print(f"链接：{link}")
            print(f"标题：{title}\n")

print("共爬取了", cnt, "条新闻")
print("类别有：", all_class)
