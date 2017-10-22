
#-*-coding:utf8-*-
__anthor__ = "ice wolf"

# 第 0003 题： 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。

import random, string
import redis

forSelect = string.ascii_letters + string.digits

def generate(count, length):
    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        print(Re)
        yield Re

def save():
    r = redis.Redis(host='127.0.0.1', port='6379')
    codes = generate(200, 20)
    p = r.pipeline()
    for code in codes:
        p.sadd('code', code)
    p.execute()
    return r.scard('code')

def main():
    print save()

if __name__ == '__main__':
    main()





