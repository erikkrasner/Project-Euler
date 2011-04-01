#!/usr/bin/env python
# 4613732
# 0.033 s

import sys
from itertools import ifilter, takewhile

def fibs():
    a,b = 1,1
    while True:
	yield b
	a,b = b,a+b

def sum_even_valued_fibs_up_to(n):
    return sum(ifilter(lambda x:not x%2,
			takewhile(lambda fib: fib <= n,
				    fibs())))

print sum_even_valued_fibs_up_to(int(sys.argv[1]) if sys.argv[1:] else 4000000)
