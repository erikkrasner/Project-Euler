#!/usr/bin/env python
# 648
# 0.08 s

import sys
from math import factorial
def digit_sum_factorial(n):
    return sum([int(ch) for ch in str(factorial(n))])

print digit_sum_factorial(int(sys.argv[1]) if sys.argv[1:] else 100)
