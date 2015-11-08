__author__ = 'Unai'


# Import the algorithms
from algs.MedianOfMedians import medianOfMedians

# Import the sequences
from tests.Sequence_Loader import random, halfsorted, sortedseq

# Import the profiling classes
import timeit

# Import useful modules
import numpy as np

lst = []
element = 0


def timeit_mom():
    medianOfMedians(lst, element)


def test_mom(n):
    sizes = list(range(2, 51)) + [100, 1000, 10000, 100000, 150000]
    random_inputs = []
    halfsorted_inputs = []
    sorted_inputs = []
    for s in sizes:
        random_inputs.append(random(s))
        halfsorted_inputs.append(halfsorted(s))
        sorted_inputs.append(sortedseq(s))

    input_lists = [random_inputs, halfsorted_inputs, sorted_inputs]

    dim = 3, len(sizes), 2
    list_of_tuples = np.zeros(dim, dtype=np.float)

    it_num = 0
    for it in input_lists:
        size_num = 0
        for i in it:
            global lst
            lst = i
            global element
            element = len(i)//2
            elapsed = timeit.timeit("timeit_mom()", setup="from tests.Test_MedianOfMedians import timeit_mom", number=n)
            list_of_tuples[it_num][size_num] = [len(lst), elapsed]
            size_num += 1
        it_num += 1

    print('\t\tSaving files...')
    np.savetxt('output/mom_random.txt', list_of_tuples[0], fmt='%s')
    np.savetxt('output/mom_halfsorted.txt', list_of_tuples[1], fmt='%s')
    np.savetxt('output/mom_sorted.txt', list_of_tuples[2], fmt='%s')

