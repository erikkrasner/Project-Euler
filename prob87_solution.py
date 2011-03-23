#!/usr/bin/env python
from itertools import takewhile
from itertools import chain
def primes():
    for line in chain(open('primes1.txt','r'),open('primes2.txt','r')):
        for prime in map(int,line.split()):
            yield prime

def squarecubefourth(n):
    squareables = map(lambda x:x,takewhile(lambda p: p **2 + 2 ** 3 + 2 ** 4 < n,primes()))
    cubeables = filter(lambda p: 2**2 + p ** 3 + 2 ** 4 < n, squareables)
    fourthables = filter(lambda p: 2**2 + 2**3 + p**4 < n, cubeables)
    results = set()
    for p1 in fourthables:
        fourth = p1**4
        for p2 in cubeables:
            cube = p2**3
            for p3 in squareables:
                square = p3**2
                if square + cube + fourth < n:
                    results.add(square + cube + fourth)
                else:
                    break
            if cube + fourth + 4 > n:
                break
    return len(results)

print squarecubefourth(50000000)
