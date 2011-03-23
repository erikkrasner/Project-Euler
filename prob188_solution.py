#!/usr/bin/env python
# 23786737
# 4.3 s

def modexp(a,b,m):
	power = 1
	while b:
		power *= a
		power %= m
		b -= 1
	return power

def modtetrate(a,b,m):
	tetration = a
	b -= 1
	while b:
		tetration = modexp(tetration,a,m)
		b -= 1
	return tetration

print modtetrate(1777,1855,10**8)
