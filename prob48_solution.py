#!/usr/bin/env python
# 9110846700
# 1.043 s

import sys

def modexp(a,b,m):
	power = 1
	while b:
		power *= a
		power %= m
		b -= 1
	return power

def sum_all_modexps(minimum,maximum,mod):
	return sum([modexp(x,x,mod) for x in range(minimum,maximum + 1)]) % mod

print sum_all_modexps(1,(sys.argv[1] if sys.argv[1:] else 1000),10**10)
