#!/usr/bin/env python
# 95962097
# 0.098s

def modtetrate(a,b,m):
	tetration = a
	half = 1
	while 2 * half < b:
		tetration = pow(tetration,tetration,m)
		half *= 2
	b -= 1
	while b >= half:
		tetration = pow(a,tetration,m)
		b -= 1
	return tetration

print modtetrate(1777,1855,10**8)
