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
        elif m > k:
            return quickSelectRnd(smallerList, k)
        else:
            return quickSelectRnd(largerList, k-m-count)
