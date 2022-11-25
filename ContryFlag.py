import requests
from bs4 import BeautifulSoup
url = 'https://zh.wikipedia.org/zh-tw/%E5%90%84%E5%9B%BD%E5%AE%B6%E5%92%8C%E5%9C%B0%E5%8C%BA%E4%BA%BA%E5%8F%A3%E5%88%97%E8%A1%A8'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
table = sp.find('table', class_='wikitable sortable')
element = table.find_all('span',class_='flagicon') #len(246)

#抓取imgurl
imgurl_l = []
for i,item in enumerate(element):
    imgurl = element[i].select('img')[0].get('src')
    imgurl_l.append(imgurl)

#將小圖url取代為大圖480url
for i,item in enumerate(imgurl_l):
    pos = item.find('px')
    imgurl_l[i] = 'https:' + item.replace(item[(pos-2):pos],'480')

#抓圖片檔名
title_l = []
title_td = table.find_all('td') #第7個開始每次跳6

for i in range(7,len(title_td),6):
    title_l.append(title_td[i].select('a')[0].get('title'))

###抓圖片&存檔###
# 存檔路徑
path = r'D:\Python\Program\DB and Web crawler\20221123\Image\\'


for i, item in enumerate(imgurl_l):
    r = requests.get(item)  # 到圖片網頁去
    with open(path + title_l[i] + '.jpg', 'wb') as f:
        f.write(r.content)  # 存檔
