#!/usr/bin/env python
# 906609
# 1.689 s

import sys
import heapq

def descending_products_from(minimum, maximum):
    products = [(-(maximum * maximum),maximum)]
    small_multiplicand = maximum
    while products:
	product,multiplicand = heapq.heappop(products)
	yield -product
	if small_multiplicand > minimum and multiplicand == small_multiplicand:
	    small_multiplicand -= 1
	    for big_multiplicand in xrange(maximum,small_multiplicand - 1,-1):
		heapq.heappush(products,(-(small_multiplicand * big_multiplicand),small_multiplicand))

def palindromic(n):
    if type(n) is not str:
	n = str(n)
    left,right = 0,len(n)-1
    while left < right:
	if n[left] != n[right]:
	    return False
	left,right = left+1,right-1
    return True

def largest_palindromic_n_digit_product(n):
    for product in descending_products_from(10**(n-1),(10**n)-1):
	if palindromic(product):
	    return product

print largest_palindromic_n_digit_product(int(sys.argv[1]) if sys.argv[1:] else 3)
