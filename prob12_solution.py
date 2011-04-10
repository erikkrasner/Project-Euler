#!/usr/bin/env python
# 76576500
# 39.906 s

from itertools import count, takewhile
import sys

def has_over_n_divisors(num,n):
    sqrt = int(num**0.5)
    total = 0
    for x in xrange(1,sqrt):
	if not num % x:
	    total += 1 if x * x == num else 2
	if total > n:
	    return True
	if total + (sqrt - x) < n:
	    return False
    return False

def triangles():
    for n in count(1):
	yield n * (n + 1) / 2

def first_triang_over_n_divisors(n):
    for t in triangles():
	if has_over_n_divisors(t,n):
	    return t

print first_triang_over_n_divisors(int(sys.argv[1]) if sys.argv[1:] else 500)
