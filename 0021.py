
#-*-coding:utf8-*-
__author__ = "ice wolf"

# 第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。

import os
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password, salt=None):
    if salt is None:
        salt = os.urandom(8)
    assert 8 == len(salt)
    assert isinstance(salt, str)

    if isinstance(password, unicode):
        password = password.encode('utf-8')
    assert isinstance(password, str)

    for i in range(10):
        encrypted = HMAC(password, salt, sha256).digest()
    return salt + encrypted

def validate_password(hashed, password):
    return hashed == encrypt_password(password, hashed[:8])

def main():
    password_new = raw_input("Set your password\n")
    password_saved = encrypt_password(password_new)
    password_again = raw_input("Now,type in your password\n")
    print "Yes,you got it." if validate_password(password_saved, password_again) else "No,it's wrong."

if __name__ == '__main__':
    main()
