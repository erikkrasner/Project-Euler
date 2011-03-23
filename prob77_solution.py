#!/usr/bin/env python
# 71
# 4 seconds reading prime list from file

from itertools import count
from itertools import takewhile

prime_file = open('primes1.txt','r')
prime_list = []
for line in prime_file:
    prime_list += map(int, line.split())
prime_set = set(prime_list)

def first_prime_sum_exceeding(prime_sum_count):
	prime_sums = {}
	def num_prime_sums(n):
		return num_prime_sums_helper(n,2)
	def num_prime_sums_helper(n,smallest_prime):
		if n < smallest_prime:
			return 0
		if (n, smallest_prime) in prime_sums:
			return prime_sums[(n, smallest_prime)]
		if n in prime_set:
			num_sums = 1
			prime_sums[(n,n)] = 1
		else:
			num_sums = 0
		primes_ascending = []
		for prime in takewhile(lambda p: p <= n, prime_list):
			primes_ascending.append(prime)
		primes_descending = primes_ascending[::-1]
		for prime in primes_descending:
			num_sums += num_prime_sums_helper(n - prime, prime)
			prime_sums[(n,prime)] = num_sums
		return num_sums
	for n in count(2):
		if num_prime_sums(n) > prime_sum_count:
			return n

print first_prime_sum_exceeding(5000)
