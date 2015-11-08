__author__ = 'Unai'

from tests.Test_MedianOfMedians import test_mom
from tests.Test_QuickselectFirst import test_qsFirst
from tests.Test_QuickselectRandom import test_qsRandom
from tests.Test_RandomAlgorithm import test_rndAlg


if __name__ == "__main__":
    print('START\n\tStart of: Median of medians')
    #test_mom(1)
    print('\tEnd of: Median of medians\n\tStart of: QS First Pivot')
    #test_qsFirst(1)
    print('\tEnd of: QS First Pivot\n\tStart of: QS Random Pivot')
    test_qsRandom(1000)
    print('\tEnd of: QS Random Pivot\n\tStart of: Random Algorithm')
    #test_rndAlg(1000)
    print('\tEnd of: Random Algorithm\nEND')


