#!/usr/bin/env python
# 18613426663617118
# 21.406s

import sys
from itertools import dropwhile
from prime_gen import *

def extended_gcd(a,b):
	x,y,lastx,lasty=0,1,1,0
	while b:
		quotient = a / b
		a,b = b,a%b
		x,lastx = lastx-quotient*x,x
		y,lasty = lasty-quotient*y,y
	return (lastx,lasty,a)

def inverse_a_mod_b(a,b):
	inverse = extended_gcd(a,b)[0] % b
	assert a * inverse % b == 1
	return inverse

def S(p1,p2,power_of_ten):
	assert p1 < p2
	assert power_of_ten > p1
	first_digits = (p2 - p1) * inverse_a_mod_b(power_of_ten,p2) % p2
	s = p1 + power_of_ten * first_digits
	assert not s % p2
	assert s % power_of_ten == p1
	return s

def sigma_s(n):
	sigma = 0
	p1,p2 = 5,7
	power_of_ten = 10
	prime_iter = dropwhile(lambda n: n <= 7,primes())
	while p1 <= n:
		while power_of_ten < p1:
			power_of_ten *= 10
		sigma += S(p1,p2,power_of_ten)
		p1,p2 = p2,prime_iter.next()
	return sigma

if __name__ == '__main__':
    print sigma_s(sys.argv[1] if sys.argv[1:] else 1000000)
