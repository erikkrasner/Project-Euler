#!/usr/bin/env python
# 1366
# 0.05 s

import sys

def digit_sum_two_to_the(n):
    return sum([int(ch) for ch in str(2**n)])

print digit_sum_two_to_the(int(sys.argv[1]) if sys.argv[1:] else 1000)
