#!/usr/bin/env python
# 142857
# 2.95 s

from itertools import count
import sys

def is_permutation(int1,int2):
	return sorted(str(int1)) == sorted(str(int2))

#can be optimized further by breaking the computation
# if one multiple is not a permutation
def smallest_integer_permutation_of(max_multiple):
	for x in count(1):
            matches = True
            for multiple in range(2,max_multiple + 1):
                if not is_permutation(x,multiple * x):
                    matches = False
                    break
            if matches: return x

print smallest_integer_permutation_of(sys.argv[1] if sys.argv[1:] else 6)
