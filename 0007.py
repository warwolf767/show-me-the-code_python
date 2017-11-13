
#-*-coding:utf8-*-
__author__ = "ice wolf"

# 第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

import os
import re

def statCode(dirPath):
    if not os.path.isdir(dirPath):
        return
    expRe = re.compile(r'^#.*')
    fileList = os.listdir(dirPath)
    print("%s\t%s\t%s\t%s" % ('file', 'all_lines', 'space_lines', 'exp_lines'))
    for file in fileList:
        filePath = os.path.join(dirPath, file)
        if os.path.isfile(filePath) and os.path.splitext(filePath)[1] == '.py':
            with open(filePath) as f:
                allLines = 0
                spaceLines = 0
                expLines = 0
                for line in f.readlines():
                    allLines += 1
                    if line.strip() == '':
                        spaceLines += 1
                        continue
                    exp = expRe.findall(line.strip())
                    if exp:
                        expLines += 1
            print("%s\t%9s\t%11s\t%8s" % (file, allLines, spaceLines, expLines))

def main():
    statCode('.')

if __name__ == '__main__':
    main()
