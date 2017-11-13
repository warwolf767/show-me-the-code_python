
#-*-coding:utf8-*-
__author__ = "ice wolf"

# 第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。

import re

def main():
    fin = open('test-E.txt', 'r')
    str = fin.read()
    reObj = re.compile('\b?(\w+)\b?')
    words = reObj.findall(str)
    wordDict = dict()
    for word in words:
        if word.lower() in wordDict:
            wordDict[word.lower()] += 1
        else:
            wordDict[word.lower()] = 1

    for key, value in wordDict.items():
        print('%s: %s' % (key, value))

if __name__ == '__main__':
    main()
