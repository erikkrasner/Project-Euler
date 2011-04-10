#!/usr/bin/env python
# 4782
# 2.064 s

import sys

def num_digits(n):
    return len(str(n))

def fibs():
    a,b = 1,1
    while True:
	yield a
	a,b = b,a+b

def first_fib_n_digits(n):
    for index,fib in enumerate(fibs()):
	if num_digits(fib) >= n:
	    return index + 1

print first_fib_n_digits(int(sys.argv[1]) if sys.argv[1:] else 1000)
