#!/usr/bin/env python
# 2783915460
# 0.218 s

from itertools import permutations,islice
import sys

def nth_permutation_of_ten_digits(n):
    permutation_iter = permutations(range(10))
    for perm in islice(permutation_iter,n):
	pass
    return ''.join([str(digit) for digit in perm])

print nth_permutation_of_ten_digits(int(sys.argv[1])\
                                    if sys.argv[1:] else 1000000)
