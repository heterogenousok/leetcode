#!/usr/bin/python
# author luke
import random
import time


class MySort:
    def __init__(self, arr_num=10, num_range=100):
        # 默认情况下是10个数
        if arr_num == 10:
            temp_list = '3 87 2 93 78 56 61 38 12 40'.split()
            self.arr = [int(i) for i in temp_list]
        else:
            self.arr = []
            for i in range(arr_num):
                self.arr.append(random.randint(0, num_range - 1))
        self.arrlen = arr_num
        self.arr1 = self.arr.copy()
        self.num_range = num_range

    def bubble(self):
        arr = self.arr
        i = self.arrlen
        while i > 1:  # i代表的是无序数的数目
            j = 0  # 内层控制比较，每次都从头比较
            while j < i - 1:
                if arr[j] > arr[j + 1]:  # 比较
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j += 1
            i -= 1

    def select(self):
        arr = self.arr
        i = 0
        while i < self.arrlen - 1:  # 控制的是无序数数目的起始位置
            min_pos = i
            j = min_pos + 1
            while j < self.arrlen:  # 找到所有的无序数中最小值位置的下标
                if arr[j] < arr[min_pos]:
                    min_pos = j
                j += 1
            arr[i], arr[min_pos] = arr[min_pos], arr[i]  # 让最小值和开头进行交换
            i += 1

    def insert(self):
        arr = self.arr
        i = 1  # 第一个要插入的数的位置
        while i < self.arrlen:
            insert_val = arr[i]
            j = i - 1  # 有序序列的最后一个位置
            while j >= 0:
                if insert_val < arr[j]:
                    arr[j + 1] = arr[j]
                else:
                    break
                j -= 1
            arr[j + 1] = insert_val  # 一定要把赋值放到break后
            i += 1

    def shell(self):
        arr = self.arr
        # 先把插入排序复制一遍，把所有为1的地方，都改为gap，除了i+=1
        # 最外层循环控制步长
        gap = self.arrlen >> 1
        while gap > 0:
            i = gap  # 第一个要插入的数的位置
            while i < self.arrlen:
                insert_val = arr[i]
                j = i - gap  # 有序序列的最后一个位置
                while j >= 0:
                    if insert_val < arr[j]:
                        arr[j + gap] = arr[j]
                    else:
                        break
                    j -= gap
                arr[j + gap] = insert_val  # 一定要把赋值放到break后
                i += 1  # 只有这一个地方不是gap
            gap >>= 1

    def partition(self, left, right):
        arr = self.arr
        # k始终指向比分割值小的数要放置的位置的下标
        k = left
        for i in range(left, right):
            # 如果元素小于分割值，就交换
            if arr[i] < arr[right]:
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def quick(self, left, right):
        if left < right:
            # pivot 是分割值的下标
            pivot = self.partition(left, right)
            self.quick(left, pivot - 1)
            self.quick(pivot + 1, right)

    def adjust_max_heap(self, adjust_pos, arr_len):
        arr = self.arr
        dad = adjust_pos
        son = 2 * dad + 1  # 左孩子
        while son < arr_len:
            if son + 1 < arr_len and arr[son] < arr[son + 1]:  # 拿大的孩子跟父亲比
                son += 1
            if arr[son] > arr[dad]:
                arr[son], arr[dad] = arr[dad], arr[son]  # 孩子比父亲大，要交换
                dad = son
                son = 2 * dad + 1
            else:
                break

    def heap(self):
        arr = self.arr
        # 把堆调整为大顶堆，大根堆
        for i in range(self.arrlen // 2 - 1, -1, -1):
            self.adjust_max_heap(i, self.arrlen)
        # 交换堆顶元素和数组最后一个元素
        arr[0], arr[self.arrlen - 1] = arr[self.arrlen - 1], arr[0]
        for i in range(self.arrlen - 1, 1, -1):  # 让数组长度不断缩小
            self.adjust_max_heap(0, i)
            arr[0], arr[i - 1] = arr[i - 1], arr[0]  # 让顶部元素和最后一个元素交换

    def merge_arr(self, low, mid, high):
        arr = self.arr
        arr_t = self.arr1
        # 把原数组数据往临时数组当中复制一下
        for i in range(low, high + 1):
            arr_t[i] = arr[i]
        i = low
        j = mid + 1
        k = low
        # 比较两个有序数组，进行合并
        while i <= mid and j <= high:
            if arr_t[i] < arr_t[j]:
                arr[k] = arr_t[i]
                i += 1
                k += 1
            else:
                arr[k] = arr_t[j]
                j += 1
                k += 1
        # 把某一个有序数组的剩余元素放入arr
        while i <= mid:
            arr[k] = arr_t[i]
            i += 1
            k += 1
        while j <= high:
            arr[k] = arr_t[j]
            j += 1
            k += 1

    def merge(self, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge(low, mid)
            self.merge(mid + 1, high)
            self.merge_arr(low, mid, high)

    def count_time(self, method, *args):
        '''
        统计每一种排序算法的时间
        :return:
        '''
        start = time.time()
        method(*args)
        end = time.time()
        print(end - start)

    def count_sort(self):
        arr = self.arr
        count = [0] * self.num_range
        # 统计每个数出现的次数
        for i in arr:
            count[i] += 1
        # 如何根据出现的次数，回填原数组
        k = 0
        # 根据每个数出现的次数，回填到原数组
        for i in range(self.num_range):
            for j in range(count[i]):
                arr[k] = i
                k += 1


if __name__ == '__main__':
    # 除了计数排序外，最大搞到1000万
    a = MySort(10)
    print(a.arr)
    # a.bubble()
    # a.select()
    # a.insert()
    # a.shell()
    # a.quick(0, a.arrlen - 1)
    # a.heap()
    # a.merge(0, a.arrlen - 1)
    a.count_sort()
    print(a.arr)
    # 统计时间
    # a.count_time(a.count_sort)
