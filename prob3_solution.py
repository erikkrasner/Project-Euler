#!/usr/bin/env python
# 6857
# 0.402 s

import sys
from prime_gen import *

def largest_prime_factor(n):
    for p in primes():
	while not n % p:
	    n /= p
        if n == 1:
	    return p
	if p * p > n:
	    return n

print largest_prime_factor(int(sys.argv[1]) if sys.argv[1:] else 600851475143)
