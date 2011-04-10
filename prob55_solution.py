#!/usr/bin/env python
# 249
# 0.605 s

def reverse(n):
    return int(`n`[::-1]) if type(n) is int else long(`n`[:-1][::-1])

def palindromic(n):
    return n == reverse(n)

def lychrel(n):
    for _ in range(50):
	n = n + reverse(n)
	if palindromic(n):
	    return False
    return True

print len([n for n in range(1,10000) if lychrel(n)])
