__author__ = 'Unai'

import random


def partition(lst, left, right, pivotIndex):
    pivotValue = lst[pivotIndex]
    lst[pivotIndex], lst[right] = lst[right], lst[pivotIndex]  # Move pivot to end

    storeIndex = left
    for i in range(left, right):
        if lst[i] < pivotValue:
            lst[storeIndex], lst[i] = lst[i], lst[storeIndex]
            storeIndex += 1
    lst[right], lst[storeIndex] = lst[storeIndex], lst[right]  # Move pivot to its final place
    return storeIndex


def quickSelectRnd(lst, left, right, n):
    while left != right:
        pivotIndex = random.randint(left, right)
        pivotIndex = partition(lst, left, right, pivotIndex)
        if n == pivotIndex:
            return lst[n]
        elif n < pivotIndex:
            right = pivotIndex - 1
        else:
            left = pivotIndex + 1
    return lst[left]
