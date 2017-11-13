
#-*-coding:utf8-*-
__author__ = "ice wolf"

# 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

def main():
    word_filter = set()
    with open('filtered_words.txt') as f:
        for w in f.readlines():
            word_filter.add(w.strip())

    while True:
        s = input()
        if s == 'exit':
            break
        if s in word_filter:
            print('Freedom')
        else:
            print('Human Rights')

if __name__ == '__main__':
    main()
