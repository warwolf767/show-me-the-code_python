
#-*-coding:utf8-*-
__anthor__ = "ice wolf"

# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

import random, string
import MySQLdb.connections

forSelect = string.ascii_letters + string.digits

def generate(count, length):
    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        print(Re)
        yield Re

def save():
    conn = MySQLdb.Connection (user='root',db='pytest')
    cursor = conn.cursor()
    codes = generate(200, 20)
    for code in codes:
        execstr = "INSERT INTO `code`(`code`) VALUES('" + str(code) + "')"
        cursor.execute(execstr)
    conn.commit()
    cursor.close()

def main():
    save()

if __name__ == '__main__':
    main()



