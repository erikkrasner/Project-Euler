#!/usr/bin/env python
# 510510
# 0.057 s
import sys
from itertools import takewhile, ifilter

prime_list = [2,3]

def count(init,step):
    while(True):
	yield init
	init += step
	
def prime(n):
    if not n % 2 or n == 1:
	return False
    for p in takewhile(lambda x: x * x <= n, prime_list):
	if not n % p:
	    return False
    while prime_list[-1] * prime_list[-1] < n:
	for odd_number in count(prime_list[-1] + 2,2):
	    if prime(odd_number):
		prime_list.append(odd_number)
		if not n % odd_number:
                    return False
		break
    return True

def primes():
    for pr in prime_list:
        yield pr
    for pr in ifilter(prime,count(prime_list[-1]+2,2)):
        yield pr

def max_totient_ratio_in_range(max_n):
	maximizing_num = 1
	for prime in primes():
		product = maximizing_num * prime
		if product > max_n:
			return maximizing_num
		maximizing_num = product

print max_totient_ratio_in_range(int(sys.argv[1]))
