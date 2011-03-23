#!/usr/bin/env python
# 248155780267521
# 0.027 seconds :)
import heapq
import time
import sys

# Generator for perfect squares, cubes, fourths, etc. in order from
#  smallest to largest, i.e. all 2^n, 3^n, etc. with n >= 2.
#  For this problem, we only need to admit b^n where b is a possible
#  digit sum for subsequent perfect powers returned by the generator.
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
	power_of_ten, ten_exponent = 10,1 # for efficient bookkeeping
	while(True):
		yield (power, base)
		power, base = heapq.heappushpop(powers,(power_iterator(base).next(),base))
		if base == max_base():
                        next_exponent_upper_bound = base * power # the largest base seen so far, times
                                                                 #  the largest power seen so far, is an
                                                                 #  upper bound for the next power
                        if next_exponent_upper_bound > power_of_ten: # we need to admit more bases and
                                                                     # update the power of ten
                                max_possible_digit_sum_lower_bound = 9 * ten_exponent # if the upper bound for the next power
                                                                                        # has n digits, its digit sum cannot
                                                                                        # exceed 9n
                                current_max_base = base
                                # add a powers_of iterator for every base up to 9n
                                while current_max_base <= max_possible_digit_sum_lower_bound:
                                        power_iterators.append(powers_of(current_max_base + 1))
                                        heapq.heappush(powers,(power_iterator(current_max_base + 1).next(),current_max_base + 1))
                                        current_max_base += 1
                                # update bookkeeping
                                ten_exponent += 1
                                power_of_ten *= 10

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
