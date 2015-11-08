__author__ = 'Unai'

# Import the algorithm
from algs.MedianRandomAlg import try_rndAlg

# Import the sequences
from tests.Sequence_Loader import random, halfsorted, sortedseq

# Import the profiling classes
import timeit

# Import useful modules
import numpy as np

lst = []


def timeit_rndAlg():
    try_rndAlg(lst)


def test_rndAlg(n):
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
    list_of_errors = np.zeros(dim, dtype=np.int)
    it_num = 0
    for it in input_lists:
        size_num = 0
        for i in it:
            global lst
            lst = i
            errors = 0
            total_elapsed = 0
            for t in range(1, n+1):
                if try_rndAlg(lst) < 0:
                    errors += 1
                else:
                    elapsed = timeit.timeit("timeit_rndAlg()",
                                            setup="from tests.Test_RandomAlgorithm import timeit_rndAlg", number=1)
                    total_elapsed += elapsed
            if errors > 0:
                if errors == n:
                    list_of_tuples[it_num][size_num] = [int(len(lst)), 0]
                else:
                    list_of_tuples[it_num][size_num] = [int(len(lst)), total_elapsed/(n-errors)]
            else:
                list_of_tuples[it_num][size_num] = [int(len(lst)), total_elapsed/n]
            list_of_errors[it_num][size_num] = [int(len(lst)), errors]
            size_num += 1
        it_num += 1

    print('\t\tSaving files...')

    np.savetxt('output/rndAlg_random.txt', list_of_tuples[0], fmt='%s')
    np.savetxt('output/rndAlg_halfsorted.txt', list_of_tuples[1], fmt='%s')
    np.savetxt('output/rndAlg_sorted.txt', list_of_tuples[2], fmt='%s')

    np.savetxt('output/rndAlg_errors_random.txt', list_of_errors[0], fmt='%i')
    np.savetxt('output/rndAlg_errors_halfsorted.txt', list_of_errors[1], fmt='%i')
    np.savetxt('output/rndAlg_errors_sorted.txt', list_of_errors[2], fmt='%i')
