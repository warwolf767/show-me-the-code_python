
#-*-coding:utf8-*-
__author__ = "ice wolf"

# 第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import random, string

forSelect = string.ascii_letters + string.digits

def generate(count, length):
    # count = 200
    # length = 20
    f = open("CDKEY.txt",'a+')
    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        print(Re)
        f.writelines(Re)

def main():
    generate(200, 20)

if __name__ == '__main__':
    main()
