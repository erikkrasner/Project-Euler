#!/usr/bin/env python
import heapq
import time
import sys

def perfect_powers_in_order(smallest_base):
	def powers_of(base):
		power = base * base
		while(True):
			yield power
			power *= base
	power_iterators = [powers_of(smallest_base)]
	def power_iterator(base):
		return power_iterators[base - smallest_base]
	max_base = lambda: len(powers) + smallest_base - 1
	powers = [(power_iterator(smallest_base).next(),smallest_base)]
	power, base = powers[0]
	while(True):
		yield (power, base)
		power, base = heapq.heappushpop(powers,(power_iterator(base).next(),base))
		if base == max_base():
			power_iterators.append(powers_of(base + 1))
			heapq.heappush(powers,(power_iterator(base + 1).next(),base + 1))

def digit_sum_perfect_powers():
	def digit_sum(n):
		total = 0
		while n:
			total += (n % 10)
			n /= 10
		return total
	for perfect_power, base in perfect_powers_in_order(6):
		if digit_sum(perfect_power) == base:
			yield perfect_power

def nth_digit_sum_perfect_power(n):
	orig_time = time.time()
	for count, dspp in enumerate(digit_sum_perfect_powers()):
		print count + 1, dspp, time.time() - orig_time
		if count + 1 == n:
			return dspp

print nth_digit_sum_perfect_power(int(sys.argv[1]))
