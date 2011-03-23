import math
def smallest_n_digit_nth_power(n):
	return math.ceil((10**(n-1))**(1.0/n))
def num_n_digit_nth_powers(n):
	print smallest_n_digit_nth_power(n)
	return 10 - smallest_n_digit_nth_power(n)
print sum(map(num_n_digit_nth_powers,range(1,23)))
