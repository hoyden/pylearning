#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Ti
@contact: hoyden_cm@163.com
@software: PyCharm
@file: 1-1.py
@time: 2017/8/15 17:32
'''

i = 3 #验证三次
file_obj = open("information.txt", "r")
lines = file_obj.readlines()
username = lines[0].strip()
password = lines[1].strip()
file_obj.close()

while i > 0:
    name = input("Please input your username:")
    pw = input("Please input your password:")
    if name == username and pw == password:
        print("Congratulations!")
        break
    else:
        i = i - 1
        print("Wrong username or password, and you have %d chances to try again!" % i)
if i == 0:
    print("Your account has been locked!")