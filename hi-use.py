#!/usr/bin/python
# author luke
import re
ret = re.search(r"\d+", "阅读次数为 9999次，理解了3次")
print(ret.group())

ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
print(ret)


#sub使用
s = 'hello world, now is 2020/7/20 18:48, 现在是2020年7月20日18时48分。'
ret_s = re.sub(r'年|月', r'/', s)
ret_s = re.sub(r'日', r' ', ret_s)
ret_s = re.sub(r'时|分', r':', ret_s)
print(ret_s)

# findall 有问题，findall在去使用时，如果里边出现了分组
com = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]')
ret = com.findall(ret_s)
print(ret)

# search 没问题
ret1 = re.search(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]', ret_s)
print(ret1.group())

#传递函数给sub
def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)

ret = re.sub(r"\d+", add, "python = 997")
print(ret)

ret = re.sub(r"\d+", add, "python = 99")
print(ret)