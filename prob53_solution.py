#!/usr/bin/env python
# 4075
# 0.07 s

import sys, operator, math
from itertools import imap

def num_n_choose_r_greater_than(n, min_result):
    r = n / 2
    # n C r = (n! / (n-r)!) / r!
    # = product n-r+1 to n / r!
    n_choose_r = reduce(operator.mul,range(n,n-r,-1),1) / math.factorial(r)
    count = 0
    while n_choose_r > min_result:
        # n C r == n C (n-r)
	count += (1 if r * 2 == n else 2)
	# n C r / n C (r - 1) =
	#  (n - r + 1) / r
	n_choose_r /= (n - r + 1)
	n_choose_r *= r
	r -= 1
    return count

def total_num_n_choose_r_greater_than(max_n,min_result):
	return sum(imap(
            lambda n: num_n_choose_r_greater_than(n,min_result),
            xrange(1,max_n+1)))

print total_num_n_choose_r_greater_than(
    int(sys.argv[1]) if sys.argv[1:] else 100,1000000)
