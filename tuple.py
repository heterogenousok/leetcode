#!/usr/bin/python
# author luke

a=tuple(i for i in range(5))
print(a)
import random
s=set()
for i in range(50):
    s.add(random.randint(0,99))

print(s)