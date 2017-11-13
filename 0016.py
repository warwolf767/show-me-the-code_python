
#-*-coding:utf8-*-
__author__ = "ice wolf"

# 第 0016 题： 纯文本文件 numbers.txt,请将内容写到 numbers.xls 文件中


from collections import OrderedDict

import xlwt,json

def main():
    with open('numbers.txt', 'r') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)
        workbook = xlwt.Workbook()
        sheet1 = workbook.add_sheet('numbers', cell_overwrite_ok=True)
        for index,values in enumerate(data):
            for i, value in enumerate(values):
                sheet1.write(index, i, value)
        workbook.save('numbers.xls')

if __name__ == '__main__':
    main()
