#!/usr/bin/python
# author luke

#常量会用大写的来命名
MAXKEY=1000

def elf_hash(hash_str):
    h = 0
    g = 0
    for i in hash_str:
        h = (h << 4) + ord(i)
        g = h & 0xf0000000
        if g:
            h ^= g >> 24
        h &= ~g
    return h % MAXKEY

def use_hash():
    str_list = ["xiongda", "lele", "hanmeimei", "wangdao", "fenghua"]
    #定义一个hash 表
    hash_table=[0]*MAXKEY
    for i in str_list:
        key=elf_hash(i)  #算出key值的过程，就是哈希，哈希就是散列
        if hash_table[key]==0:
            hash_table[key]=i
        else:
            print('哈希冲突')
    pass

if __name__ == '__main__':
    use_hash()
    hash('xiongda') #两次启动不一样，是因为加入了盐值
    #时间复杂度是O(1)  空间复杂度不是O(1)