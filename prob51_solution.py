#!/usr/bin/env python
# 121313
# 36.0 s
from itertools import combinations
from prime_gen import *

def digits_and_positions(number):
	digits = [int(digit) for digit in str(number)]
	positions = {}
	for position, digit in enumerate(digits):
		if digit not in positions:
			positions[digit] = []
		positions[digit].append(position)
	return positions

def subsets(list):
	for length in range(1,len(list)+1):
		for combination in combinations(list,length):
			yield combination

def mask(number, positions):
	mask = ''
	num_string = str(number)
	for position in range(len(num_string)):
		mask += (num_string[position] if position in positions else 'x')
	return mask

def first_prime_family(target_size):
	prime_families = {}
	for prime in primes():
		all_positions = set(range(len(str(prime))))
		total_length = len(str(prime))
		positions_dict = digits_and_positions(prime)
		for digit in positions_dict:
			for position_set in subsets(positions_dict[digit]):
				other_digits = all_positions - set(position_set)
				msk = mask(prime,other_digits)
				if msk not in prime_families:
					prime_families[msk] = {}
				family = prime_families[msk]
				if digit not in family:
					family[digit] = prime
				if len(family) == target_size:
					return family

print min(first_prime_family(8).values())
