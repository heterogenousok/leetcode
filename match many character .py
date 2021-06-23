#!/usr/bin/python
# author luke

import re

ret = re.match("[A-Z][a-z]*","MM")
print(ret.group())

ret = re.match("[A-Z][a-z]*","MnnM")
print(ret.group())

ret = re.match("[A-Z][a-z]*","Aabcdef")
print(ret.group())

print('-'*50)
# 需求：匹配出，变量名是否有效


names = ["name1", "_name", "2_name", "__name__"]

for name in names:
    ret = re.match("[a-zA-Z_]+[\w]*",name)
    if ret:
        print("变量名 %s 符合要求" % ret.group())
    else:
        print("变量名 %s 非法" % name)

print('-'*50)
# 需求：匹配出，0到99之间的数字
#coding=utf-8
import re

ret = re.match("[1-9]?[0-9]","7")
print(ret.group())

ret = re.match("[1-9]?\d","33")
print(ret.group())

#匹配0-99，不要01和09
ret = re.match("[1-9]?\d$","9")
print(ret.group())
print('-'*50)
#匹配m个字符
ret = re.match("[a-zA-Z0-9_]{6}","12a3g45678")
print(ret.group())

ret = re.match("[a-zA-Z0-9_]{8,20}","1ad12f23s34455ff6677777777")
print(ret.group())