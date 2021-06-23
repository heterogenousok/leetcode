#!/usr/bin/python
# author luke

# 需求：匹配出0-100之间的数字
#coding=utf-8

import re

ret = re.match("[1-9]?\d","8")
print(ret.group())  # 8

ret = re.match("[1-9]?\d","78")
print(ret.group())  # 78

# 不正确的情况
ret = re.match("[1-9]?\d","08")
print(ret.group())  # 0

# 修正之后的
ret = re.match("[1-9]?\d$|100","8")
if ret:
    print(ret.group())
else:
    print("不在0-100之间")

print('-'*50)
# 需求：匹配出163、126、qq邮箱


ret = re.match("\w{4,20}@163\.com", "test@163.com")
print(ret.group())  # test@163.com

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@126.com")
print(ret.group())  # test@126.com

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@gmail.com")
if ret:
    print(ret.group())
else:
    print("不是163、126、qq邮箱")  # 不是163、126、qq邮箱

# 不是以4、7结尾的手机号码(11位)

tels = ["13100001234", "18912344321", "10086", "18800007777"]

for tel in tels:
    ret = re.match("1\d{9}[0-35-68-9]$", tel)
    if ret:
        print(ret.group())
    else:
        print("%s 不是想要的手机号" % tel)

print('提取区号和电话号码')
ret = re.match("([^-]+)-(\d+)","010-12345678")
print(ret.group())  #print(ret.group(0)) 和不写是一致的
print(ret.group(1))
print(ret.group(2))
# print(ret.group(3))   IndexError: no such group
print('-'*50)
#匹配html标签

# 能够完成对正确的字符串的匹配
ret = re.match("<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</html>")
print(ret.group())

ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
print(ret.group())


#引用分组，确保后了后面内容和前面的分组完美匹配
test_label = "<html>hh</htmlbalabala>"
ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", test_label)
if ret:
    print(ret.group())
else:
    print("%s 这是一对不正确的标签" % test_label)

labels = ["<html><h1>www.cskaoyan.com</h1></html>", "<html><h1>www.cskaoyan.com</h2></html>"]

for label in labels:
    ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", label)
    if ret:
        print("%s 是符合要求的标签" % ret.group())
    else:
        print("%s 不符合要求" % label)

print('-'*50)
# (?P<name>) (?P=name)
ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>",
               "<html><h1>www.cskaoyan.com</h1></html>")
print(ret.group())