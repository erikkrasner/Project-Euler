#!/usr/bin/env python
# 104743
# 1.23 s

import sys
from prime_gen import *
from itertools import islice

def nth_prime_number(n):
    for p in islice(primes(),n):
        pass
    return p

print nth_prime_number(int(sys.argv[1]) if sys.argv[1:] else 10001)
