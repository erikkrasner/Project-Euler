#!/usr/bin/env python

from itertools import takewhile, ifilter, imap

prime_list = [2]
prime_set = set(prime_list)

def prime_file_iter():
    prime_file = open('primes.txt','r')
    for pr_list in imap(lambda line: map(int,line.split()),prime_file):
        for pr in pr_list:
            yield pr

file_iter = prime_file_iter()
next(file_iter) # skip 2

def count(init,step):
    while(True):
        yield init
        init += step

def prime(n):
    if n <= prime_list[-1]:
        return n in prime_set
    if not n % 2 or n == 1:
        return False
    for p in takewhile(lambda x: x * x <= n, prime_list):
        if not n % p:
            return False
    while prime_list[-1] * prime_list[-1] < n:
        try:
            next_prime = next(file_iter)
            prime_set.add(next_prime)
            prime_list.append(next_prime)
            if not n % next_prime:
                return False
        except StopIteration:
            for odd_number in count(prime_list[-1] + 2,2):
                if prime(odd_number):
                    prime_set.add(odd_number)
                    prime_list.append(odd_number)
                    if not n % odd_number:
                        return False
                    break
    return True

def primes():
    for pr in prime_list:
        yield pr
    for pr in file_iter:
        prime_list.append(pr)
        prime_set.add(pr)
        yield pr
    for pr in ifilter(prime,count(prime_list[-1]+2,2)):
        yield pr

