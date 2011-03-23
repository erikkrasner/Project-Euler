#!/usr/bin/env python
# 51161058134250
# 0.064 s
import sys

#dynamic programming to find number of increasing numbers with n digits
increasing_memo_table = {}
def num_increasing_numbers(num_digits):
	def num_increasing_numbers_ending_with(num_digits,last_digit):
		if last_digit == 0:
			return 0
		if num_digits == 1:
			return 1
		if (num_digits,last_digit) in increasing_memo_table:
			return increasing_memo_table[(num_digits,last_digit)]
		num = sum(map(lambda digit: num_increasing_numbers_ending_with(num_digits - 1,digit),range(last_digit+1)))
		increasing_memo_table[(num_digits,last_digit)] = num
		return num
	return sum(map(lambda last_digit:num_increasing_numbers_ending_with(num_digits,last_digit),range(10)))

#slightly different because decreasing numbers can include 0s
decreasing_memo_table = {}
def num_decreasing_numbers(num_digits):
    def num_decreasing_numbers_starting_with(num_digits,first_digit):
	if num_digits == 1:
		return 1
	if (num_digits,first_digit) in decreasing_memo_table:
		return decreasing_memo_table[(num_digits,first_digit)]
	num = sum(map(lambda digit: num_decreasing_numbers_starting_with(num_digits - 1,digit),range(first_digit+1)))
	decreasing_memo_table[(num_digits,first_digit)] = num
	return num
    return sum(map(lambda first_digit:num_decreasing_numbers_starting_with(num_digits,first_digit),range(1,10)))

def num_nonbouncy_numbers_less_than_ten_to_the(n):
	return sum(map(num_increasing_numbers,range(1,n+1))) + sum(map(num_decreasing_numbers,range(1,n+1))) - 9 * n

print num_nonbouncy_numbers_less_than_ten_to_the(int(sys.argv[1]))
