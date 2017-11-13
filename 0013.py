
#-*-coding:utf8-*-
__author__ = "ice wolf"

# 第 0013 题： 用 Python 写一个爬图片的程序

import re, urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'class="BDE_Image" src="(.+\.jpg)" '
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'13/%s.jpg' % x)
        x+=1
        print imgurl

def main():
    html = getHtml("http://tieba.baidu.com/p/1869906351")
    # print html
    getImg(html)

if __name__ == '__main__':
    main()
