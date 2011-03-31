#!/usr/bin/env python
# 232792560

import sys
from fractions import gcd

def smallest_number_divisible_by_numbers_up_to(n):
    divisible = 1
    for divisor in xrange(1,n+1):
	divisible /= gcd(divisible,divisor)
	divisible *= divisor
    return divisible

print smallest_number_divisible_by_numbers_up_to(
    int(sys.argv[1]) if sys.argv[1:] else 20)
