#!/usr/bin/env python
# 25164150

from itertools import imap
import sys

def square_sum_difference(n):
	return sum(xrange(1,n+1)) ** 2 - sum(imap(lambda x: x**2, xrange(1,n+1)))

print square_sum_difference(int(sys.argv[1]) if sys.argv[1:] else 100)
