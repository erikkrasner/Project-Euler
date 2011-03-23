#!/usr/bin/env python
from decimal import Decimal
import time
def fibonaccis():
    a,b = 0,1
    while(True):
        a,b = b,a+b
        yield a

def pandigital(digit_string):
    return sorted(digit_string) == sorted('123456789')

def last_nine_pandigital(num):
    return num > 10**8 and pandigital(str(num % 10**9))

def first_last_nine_pandigital():
    for index, fib in enumerate(fibonaccis()):
        if last_nine_pandigital(fib):
            return index + 1

def first_nine_pandigital(num):
    return num > 10**8 and pandigital(str(num)[:9])

def first_first_nine_pandigital():
    for index, fib in enumerate(fibonaccis()):
        if first_nine_pandigital(fib):
            return index + 1

def first_both_nines_pandigital():
    for index, fib in enumerate(fibonaccis()):
        if not index % 10000:
            print index, time.time() - orig_time, str(fib)[-9:]
        if last_nine_pandigital(fib) and first_nine_pandigital(fib):
            return index + 1

orig_time = time.time()
print first_both_nines_pandigital()
