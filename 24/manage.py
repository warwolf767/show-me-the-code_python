
#-*-coding:utf8-*-
__author__ = "ice wolf"

# 第 0024 题： 使用 Python 的 Web 框架，做一个 Web 版本 TodoList 应用。

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TodoList.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
