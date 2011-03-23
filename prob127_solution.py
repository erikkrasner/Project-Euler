#!/usr/bin/env python
# (18407904, 5200.6671280860901)
import time
import sys
from fractions import gcd
from itertools import takewhile
from itertools import ifilter

prime_file = open('primes1.txt','r')
prime_file.next()
prime_list = []
for line in prime_file:
    prime_list += map(int,line.split())
prime_set = set(prime_list)

def rad(number):
    if number in prime_set:
        return number
    product = 1
    for prime in prime_list:
        if prime * prime > number:
            break
        if not number % prime:
            product *= prime
            while not number % prime:
                number /= prime
    if number in prime_set:
        product *= number
    return product

rads = map(rad,range(120000))
numbers_with_smaller_rads = map(lambda pair:pair[0],filter(lambda pair: pair[1] < pair[0],enumerate(rads)))
numbers_with_smaller_rads_set = set(numbers_with_smaller_rads)

def abc_hit(a,b,c,rad_product):
    return gcd(a,b) == 1 and gcd(b,c) == 1 and rad_product * rads[b] < c

def sum_abc_hits_up_to(max_c):
    old_time = time.time()
    total = 0
    for c in takewhile(lambda x: x < max_c,numbers_with_smaller_rads):
        if not c % 1000:
            print c,total,time.time()-old_time
        for a in ifilter(lambda num:c%2 or num%2,takewhile(lambda x: x < c,numbers_with_smaller_rads)):
            rad_product = rads[a] * rads[c]
            gcd_ac = gcd(a,c)
            if gcd_ac == 1 and rad_product < c:
                b = c - a
                if abc_hit(a,b,c,rad_product):
                    if a * 2 < c:
                        total += c
                    elif b not in numbers_with_smaller_rads_set:
                        total += c
    return (total,time.time()-old_time)

if __name__ == '__main__':
    max_c = int(sys.argv[1]) if len(sys.argv) > 1 else 120000
    print sum_abc_hits_up_to(max_c)
