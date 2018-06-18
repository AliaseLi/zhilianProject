from urllib import request
from bs4 import BeautifulSoup
import settings
from item import Item
from zhaopianDB import DB


class zhaopinSpider:
    def __init__(self):
        self.db_ = DB()
        print('开始遛弯了')

    def __del__(self):
        print('感谢有你，准备回家')
        self.db_.close()

    def run(self, start_url):
        html = self.request(start_url)
        next_url = self.parse(html)

    def request(self, start_url):  #　请求数据
        req = request.Request(start_url,headers=settings.headers)
        resp = request.urlopen(req)
        if resp.status == 200:
            print('ok')
            # with open('zhaopin.html','wb') as f:
            #     f.write(resp.read())
            # print('保存成功')
            return resp.read().decode()

    def parse(self, html):   # 用bs解析数据
        soup = BeautifulSoup(html,'lxml')
        tables = soup.select('#newlist_list_content_table table')[2:]
        for table in tables:
            tr = table.find('tr')
            zwmc = tr.find('td',class_='zwmc').a.text
            gsmc = tr.find('td',class_='gsmc').a.text
            zwyx = tr.find('td',class_='zwyx').text
            gzdd = tr.find('td',class_='gzdd').text
            item = Item(zwmc, gsmc, zwyx, gzdd)
            self.save(item)
            print(item)
            print('--------------------------------')

    def save(self, item):
        self.db_.save(item)

if __name__ == '__main__':
    for p in range(1,3):
        start_url = settings.reqUrl('北京','python爬虫',p)
        zhaopinSpider().run(start_url)