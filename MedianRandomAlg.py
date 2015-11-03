__author__ = 'Unai'

import numpy as np
import math


def rndAlgMedian(lst):
    #R = a multiset of n^3/4 elements from S chosen uar with replacement
    n = len(lst)
    R = []
    n_R = math.pow(n, 3/4)
    R = np.random.choice(lst, n_R, True)

    # sort R
    list.sort(R)
    # d = R[1/2 * n^3/4 - sqrt n]
    d = R[1/2 * n_R - math.sqrt(n)]
    # u =  R[1/2 * n^3/4 - sqrt n]
    u = R[1/2 * n_R + math.sqrt(n)]

    """
    By comparing the elements of S to d and u, create C
    c = x pertenece a S, d<x<u, c es un vector que contiene elementos de S que estan entre los valores d y u
    """
    C = []
    # ld = x pertenece a S, x<d, numeric: cantidad de numeros menor que d
    ld = 0
    # lu = x pertenece a S, x>u, numeric: cantidad de numeros mayor que u
    lu = 0
    for x in lst:
        if x > d:
            ld += 1
        elif x > d:
            lu += 1
        else:
            list.append(C, x)
    # if( ld > n/2) FAIL
    if ld > n/2:
        return -1
    # if( lu > n/2) FAIL
    if ld > n/2:
        return -2
    # if( size(c) > 4*n^3/4 ) FAIL
    if len(C) > 4 * n_R:
        return -3
    # sort c
    list.sort(C)
    # return C[n/2 - ld +1]

    return C[n/2 - ld + 1]

lst = [70, 120, 170, 200]

print(rndAlgMedian(lst ))