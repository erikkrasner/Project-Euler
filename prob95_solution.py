#!/usr/bin/env python
# 14316
# 2m13.796s

import sys
from itertools import takewhile
from prime_gen import *

# factoring routine optimized for factoring a bunch
#  of numbers
def factor(n):
    if factor_table[n]:
        return factor_table[n]
    for potential_factor in primes():
        # Since potential_factor is the smallest factor for n
        #  other than 1, it's guaranteed to be prime -- and
        #  since n / potential_factor is smaller than n, it's
        #  guaranteed to be memoized. Neat, huh?
        if n % potential_factor == 0:
            factors = set((potential_factor,n))
            for other_factor in factor(n / potential_factor):
                factors.add(other_factor)
                factors.add(n / other_factor)
            return factors

def factor_numbers_up_to(n):
    factor_table[1] = set((1,))
    for pr in takewhile(lambda x: x <= n,primes()):
        factor_table[pr] = set((1,pr))
    for number in xrange(1,n+1):
        factor(number)

def proper_factor_sum(n):
        return sum(factor(n)) - n

def factor_sum_iter(n):
	while True:
		yield n
		n = proper_factor_sum(n)
		
def all_good_chains(upper_bound):
	for pr in takewhile(lambda x: x <= upper_bound,primes()):
		bad_chains.add(pr)
	for initial in xrange(4,upper_bound + 1):
		chain = []
		chain_set = set()
		for candidate in factor_sum_iter(initial):
			if candidate in bad_chains or candidate > upper_bound:
				for item in chain:
					bad_chains.add(item)
				break
			if candidate in chain_set:
				split_index = chain.index(candidate)
				for item in chain[:split_index]:
					bad_chains.add(item)
				good_chain = chain[split_index:]
				for item in good_chain:
					good_chains[item] = good_chain
				break
			chain.append(candidate)
			chain_set.add(candidate)

if __name__ == '__main__':
        upper_bound = sys.argv[1] if sys.argv[1:] else 1000000
        factor_table = [0 for _ in xrange(upper_bound+1)]
        factor_numbers_up_to(upper_bound)
        good_chains = {}
        bad_chains = set()
        all_good_chains(upper_bound)
        index = max(good_chains, key = lambda x: len(good_chains[x]))
        print min(good_chains[index])
