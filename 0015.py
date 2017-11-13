
#-*-coding:utf8-*-
__author__ = "ice wolf"

# 第 0015 题：纯文本文件 city.txt为城市信息,请将内容写到 city.xls 文件中

import xlwt,json

def main():
    with open('city.txt', 'r') as f:
        data = json.load(f)
        workbook = xlwt.Workbook()
        sheet1 = workbook.add_sheet('city', cell_overwrite_ok=True)
        for index, (key, value) in enumerate(data.items()):
            sheet1.write(index, 0, key)
            sheet1.write(index, 1, value)
        workbook.save('city.xls')

if __name__ == '__main__':
    main()
