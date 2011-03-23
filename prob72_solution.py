#!/usr/bin/env python
#303963552391
#takes about two minutes
from itertools import count
import time

factor_table = {}

# factoring routine optimized for factoring a bunch
#  of numbers
def factor(n):
    if n in factor_table:
        return factor_table[n]
    for potential_factor in count(2):
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
    prime_file = open ('primes1.txt','r')
    prime_list = []
    for line in prime_file:
        primes = map(int,line.split())
        prime_list += primes
        if primes[-1] > n:
            prime_file.close()
            break
    factor_table[1] = set((1,))
    for prime in prime_list:
        factor_table[prime] = set((1,prime))
    for number in xrange(1,n+1):
        if not number % 50000:
            print number,time.time()-old_time
        factor(number)

import time
def num_fractions_up_to(max_denominator):
    print "finding fractions"
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
