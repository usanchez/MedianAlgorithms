__author__ = 'Unai'

import numpy as np
from math import sqrt

def rndAlgMedian(lst):
    #R = a multiset of n^3/4 elements from S chosen uar with replacement
    n = len(lst)
    R = []
    n_R = n ** 0.75
    R = np.random.choice(lst, n_R+1, True) # ceil of # elements

    # sort R
    R.sort()
    print(R)
    mid_R = int((n_R+1)/2.)
    # d = R[1/2 * n^3/4 - sqrt n]
    d = R[int(mid_R - sqrt(n))+1] # ceil
    # u =  R[1/2 * n^3/4 - sqrt n]
    u = R[int(mid_R + sqrt(n))]

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
        if x < d:
            ld += 1
        elif x > u:
            lu += 1
        else:
            C.append(x)

    # Fail conditions
    if ld > n/2:
        return -1
    if ld > n/2:
        return -2
    if len(C) > 4 * n_R:
        return -3

    # sort c
    C.sort()

    # return C[n/2 - ld +1]
    return C[int(n/2.) - ld]

