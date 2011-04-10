#!/usr/bin/env python
# 71
# 0.065s

from itertools import takewhile
from prime_gen import *
from itertools import count

def first_prime_sum_exceeding(prime_sum_count):
	prime_sums = {}
	def num_prime_sums(n):
	    return num_prime_sums_helper(n,2)
	def num_prime_sums_helper(n,smallest_prime):
	    if n < smallest_prime:
		return 0
	    if (n, smallest_prime) in prime_sums:
		return prime_sums[(n, smallest_prime)]
	    if prime(n):
                num_sums = 1
		prime_sums[n,n] = 1
	    else:
		num_sums = 0
            primes_ascending = [pr for pr in takewhile(lambda p: p <= n, primes())]
            primes_descending = primes_ascending[::-1]
            for pr in primes_descending:
		num_sums += num_prime_sums_helper(n - pr, pr)
		prime_sums[n,pr] = num_sums
	    return num_sums
	for n in count(2):
	    if num_prime_sums(n) > prime_sum_count:
		return n

print first_prime_sum_exceeding(5000)
