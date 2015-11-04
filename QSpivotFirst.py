__author__ = 'Unai'


def quickSelect(lst, k):
    if len(lst) != 0:
        pivot = lst[0]
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
            return quickSelect(smallerList, k)
        else:
            return quickSelect(largerList, k-m-count)

lst = [70, 120, 170, 200, 254, 422, 42, 43, 423, 453, 523, 52, 323, 42, 3, 42, 34]


print(quickSelect(lst, len(lst) // 2))