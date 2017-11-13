
#-*-coding:utf8-*-
__author__ = "ice wolf"

# 第 0014 题： 纯文本文件 student.txt为学生信息,请将内容写到 student.xls 文件中

from collections import OrderedDict

import xlwt,json

def main():
    with open('student.txt', 'r') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)
        workbook = xlwt.Workbook()
        sheet1 = workbook.add_sheet('student', cell_overwrite_ok=True)
        for index, (key, values) in enumerate(data.items()):
            sheet1.write(index, 0, key)
            for i, value in enumerate(values):
                sheet1.write(index, i + 1, value)
        workbook.save('student.xls')

if __name__ == '__main__':
    main()
