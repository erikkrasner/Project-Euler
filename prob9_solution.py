#!/usr/bin/env python
# 31875000
# 0.094 s

import sys, operator

def pythag_triplet_adding_up_to(n):
    for c in xrange(n/3,n/2):
	c_squared = c ** 2
	for a in xrange(1,c):
	    b = n - c - a
	    if a ** 2 + b ** 2 == c_squared:
		return (a,b,c)
    return None


print reduce(operator.mul,
             pythag_triplet_adding_up_to(
                 int(sys.argv[1]) if sys.argv[1:] else 1000))
