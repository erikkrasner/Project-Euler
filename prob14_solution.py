#!/usr/bin/env python
# 837799
# 12.302s

import sys

collatz_memo = {1:1}
def collatz_chain_length(n):
	sequence = []
	while n not in collatz_memo:
		sequence.append(n)
		n = 3*n+1 if n % 2 else n / 2
	for index,item in enumerate(sequence[::-1]):
		collatz_memo[item] = collatz_memo[n] + index + 1
	return collatz_memo[sequence[0] if sequence else n]

def longest_collatz_chain(max_starter):
    max_length = 0
    best_starter = None
    for starter in xrange(1,max_starter):
        length = collatz_chain_length(starter)
        if length > max_length:
            best_starter = starter
            max_length = length
    return best_starter

print longest_collatz_chain(int(sys.argv[1]) if sys.argv[1:] else 1000000)
