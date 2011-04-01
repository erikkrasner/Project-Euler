#!/usr/bin/env python
# 233168
# 0.031 s

import sys

#brute force
#from itertools import ifilter
#def sum_multiples_of_three_or_five_below(max_n):
#   return sum(ifilter(lambda n:(not n%3) or (not n%5),xrange(1,max_n)))

#exponential speedup (shows up clearly around 1000000, no slower for 1000)
def sum_multiples_of_three_or_five_below(max_n):
    max_n -= 1
    threes = 3 * (max_n / 3) * (max_n / 3 + 1) / 2
    fives = 5 * (max_n / 5) * (max_n / 5 + 1) / 2
    both = 15 * (max_n / 15) * (max_n / 15 + 1) / 2
    return threes + fives - both

print sum_multiples_of_three_or_five_below(int(sys.argv[1]) if sys.argv[1:] else 1000)
