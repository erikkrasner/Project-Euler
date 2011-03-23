#!/usr/bin/env python
import sys
from prime_gen import *
from itertools import combinations, dropwhile

def combinations_from_infinite(infinite_iterable,r):
	finite_list = []
	for element in infinite_iterable:
		for combination in combinations(finite_list,r - 1):
			yield combination + (element,)
		finite_list.append(element)

def any_two_concatenate_prime(prime_tuple):
	for a,b in combinations(prime_tuple,2):
		str_a,str_b = str(a),str(b)
		if not (prime(int(str_a + str_b)) and prime(int(str_b + str_a))):
			return False
	return True

def first_concatenatable_primes(num_primes):
    for prime_tuple in combinations_from_infinite(dropwhile(lambda x: x ==2,primes()),num_primes):
        if any_two_concatenate_prime(prime_tuple):
            return prime_tuple

print first_concatenatable_primes(int(sys.argv[1])) if sys.argv[1:] else 5
