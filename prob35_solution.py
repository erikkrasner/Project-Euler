#!/usr/bin/env python
# 55
# 5.3 s

from itertools import takewhile
from prime_gen import *
import sys

def rotate(num,power_of_ten):
    return (num % 10 * power_of_ten) + (num / 10)

def rotations(num,power_of_ten):
    already_seen = set()
    for _ in range(len(`num`)):
        if num not in already_seen:
            yield num
        already_seen.add(num)
	num = rotate(num,power_of_ten)

def circular_primes_below(n):
    already_found_set = set()
    num_circulars = 0
    power_of_ten = 1
    for p in takewhile(lambda p: p < n,primes()):
        while p > power_of_ten * 10:
            power_of_ten *= 10
        if p not in already_found_set:
            rotation_list = [rot for rot in rotations(p,power_of_ten)]
            if all(imap(prime,rotation_list)):
                num_circulars += len(rotation_list)
                already_found_set |= set(rotation_list)
    return num_circulars

print circular_primes_below(int(sys.argv[1]) if sys.argv[1:] else 1000000)
