#!/usr/bin/env python
# 872187
# 2.489 s

from itertools import ifilter
import sys

def palindromic(string):
    return string == string[::-1]

def palindromic_both_bases(n):
    return palindromic(`n`) and palindromic(bin(n)[2:])

def sum_palindromic_both_bases(max_n):
    return sum(ifilter(palindromic_both_bases,xrange(1,max_n+1)))

print sum_palindromic_both_bases(int(sys.argv[1]) if sys.argv[1:] else 1000000)
