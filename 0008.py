
#-*-coding:utf8-*-
__author__ = "ice wolf"

# 第 0008 题： 一个HTML文件，找出里面的正文。

import requests,re, BeautifulSoup

def main():
    url = 'https://www.52pojie.cn/thread-582852-1-1.html'
    data = requests.get(url)
    r = re.findall(r'<body .*>([\s\S]*)</body>', data.text)
    print(r[0])

    print('---------------------------------------------------------------')
    soup = BeautifulSoup.BeautifulSoup (data.text)
    print(soup.body.text)

if __name__ == '__main__':
    main()
