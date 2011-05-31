#!/usr/bin/env python
#303963552391
#2m22.267s
from itertools import count, takewhile
from prime_gen import *
import time

factor_table = [0 for _ in xrange(10000001)]
                
# factoring routine optimized for factoring a bunch
#  of numbers
def factor(n):
    if factor_table[n]:
        return factor_table[n]
    for potential_factor in primes():
        # Since potential_factor is the smallest factor for n
        #  other than 1, it's guaranteed to be prime -- and
        #  since n / potential_factor is smaller than n, it's
        #  guaranteed to be memoized. Neat, huh?
        if n % potential_factor == 0:
            factors = set((potential_factor,n))
            for other_factor in factor(n / potential_factor):
                factors.add(other_factor)
                factors.add(n / other_factor)
            return factors

def factor_numbers_up_to(n):
    print "factoring"
    old_time = time.time()
    #m = 10000
    factor_table[1] = set((1,))
    for pr in takewhile(lambda x: x <= n,primes()):
        factor_table[pr] = set((1,pr))
    for number in xrange(1,n+1):
        if not number % 50000:
            print number,time.time()-old_time
        factor(number)

import time
def num_fractions_up_to(max_denominator):
    #print "finding fractions"
    old_time = time.time()
    fraction_counts = {}
    total = 0
    for denominator in xrange(2,max_denominator+1):
        if not denominator % 10000:
            print denominator, total,time.time() - old_time
        fraction_count = denominator - 1
        for fact in factor(denominator):
            if fact in fraction_counts:
                fraction_count -= fraction_counts[fact]
        fraction_counts[denominator] = fraction_count
        total += fraction_count
    return total

factor_numbers_up_to(1000000)
print num_fractions_up_to(1000000)
