__author__ = 'Unai'

import numpy as np
from math import sqrt, floor, ceil
from random import choice


def try_rndAlg(lst):
    try:
        return rndAlgMedian(lst)
    except IndexError:
        return -1


def rndAlgMedian(lst):
    #R = a multiset of n^3/4 elements from S chosen uar with replacement
    n = len(lst)
    R = []
    n_R = n ** 0.75

    # R = [choice(lst) for i in range(int(n_R)+1)] #sample(S, int(ceil(m))) #
    R = np.random.choice(lst, int(n_R)+1, True)  # ceil of # elements

    # sort R
    R.sort()

    # d = R[1/2 * n^3/4 - sqrt n]
    d = R[int(n_R/2 - sqrt(n))+1]  # ceil
    # u =  R[1/2 * n^3/4 - sqrt n]
    u = R[int(n_R/2 + sqrt(n))]

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
    if lu > n/2:
        return -2
    if len(C) > 4 * n_R:
        return -3

    # sort c
    C.sort()

    # return C[n/2 - ld +1]
    return C[n//2 - ld]

