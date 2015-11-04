__author__ = 'Unai'
import random


def quickSelectRnd(lst, k):

    if len(lst) != 0:
        random.seed()
        rnd = random.randint(0, len(lst)-1)
        pivot = lst[rnd]
        smallerList = []
        for i in lst:
            if i < pivot:
                smallerList.append(i)
        largerList = []
        for i in lst:
            if i > pivot:
                largerList.append(i)
        count = len(lst) - len(smallerList) - len(largerList)
        m = len(smallerList)
        if k >= m and k < m + count:
            return pivot
            print(pivot)
        elif m > k:
            return quickSelectRnd(smallerList, k)
        else:
            return quickSelectRnd(largerList, k-m-count)

lst = [70, 120, 170, 200, 254, 422, 42, 43, 423, 453, 523, 52, 323, 42, 3, 42, 34]


print(quickSelectRnd(lst, len(lst) // 2))