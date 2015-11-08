__author__ = 'Unai'
import numpy as np


def input_generator():
    size_list = list(range(1, 51)) + [100, 1000, 10000, 100000, 150000, 1000000]
    for s in size_list:
        lst = np.random.random_integers(low=0, high=(s+1)*2, size = s)
        np.savetxt("random/"+ str(s) + ".txt", lst, fmt='%i')
        lst[0:len(lst)/2.].sort()
        np.savetxt("halfsorted/"+ str(s) + ".txt", lst, fmt='%i')
        lst.sort()
        np.savetxt("sorted/"+ str(s) + ".txt", lst, fmt='%i')

input_generator()