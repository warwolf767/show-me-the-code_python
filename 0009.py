
#-*-coding:utf8-*-
__anthor__ = "ice wolf"

# 第 0009 题： 一个HTML文件，找出里面的链接。

import requests,BeautifulSoup

def main():
    url = 'http://www.freebuf.com/sectool/99895.html'
    data = requests.get(url)
    soup = BeautifulSoup.BeautifulSoup(data.text)
    urls = soup.findAll('a')
    for u in urls:
        print(u['href'])

if __name__ == '__main__':
    main()