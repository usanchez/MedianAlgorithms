__author__ = 'Unai'

# Import the algorithms
import MedianOfMedians, MedianRandomAlg, QSpivotFirst, QSrandomPivot

# Import the profiling classes
import cProfile
import time

# Import rest of useful classes
import math

# Load all the data

lst = [70, 120, 170, 200, 254, 422, 42, 43, 423, 453, 523, 52, 323, 42, 3, 42, 34]

len = len(lst)//2

start = time.clock()
MedianOfMedians.medianOfMedians(lst, len)
end = time.clock()
elapsed = end-start
print ("=> elasped MedianOfMedians: " + str(elapsed) + ', log: ' +str(math.log(elapsed, 2)))
