
#-*-coding:utf8-*-
__anthor__ = "ice wolf"

# 第 0019 题： 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中

import xlrd, json
from lxml import etree

def read_exl(file_name):
    exl = xlrd.open_workbook(file_name)
    exl_sheet = exl.sheet_by_name('numbers')
    data = []
    for i in range(exl_sheet.nrows):
        temp = [int(x) for x in exl_sheet.row_values(i) ]
        data.append(temp)
    return json.dumps(data, encoding='utf-8')

def save_to_xml(data, new_file_name):
    root = etree.Element('root')
    students = etree.SubElement(root, 'numbers')
    students.text = str(etree.Comment(u"""数字信息""")) + data

    student_xml = etree.ElementTree(root)
    student_xml.write(new_file_name, pretty_print=True, xml_declaration=True, encoding='utf-8')

def main():
    content = read_exl('numbers.xls')
    save_to_xml(content, 'numbers.xml')

if __name__ == '__main__':
    main()