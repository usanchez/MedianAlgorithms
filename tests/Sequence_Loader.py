__author__ = 'Unai'

# Returns the generated list foreach type of input
import numpy as np


def random(n):
    lst = np.loadtxt("input/random/" + str(n) + ".txt", dtype=int)
    return lst


def sortedseq(n):
    lst = np.loadtxt("input/sorted/" + str(n) + ".txt", dtype=int)
    return lst


def halfsorted(n):
    lst = np.loadtxt("input/halfsorted/" + str(n) + ".txt", dtype=int)
    return lst