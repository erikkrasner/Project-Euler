#!/usr/bin/env python
# 100
# 0.090 s

import operator
from fractions import Fraction

def reducible_fractions():
    for reduced_denominator in range(1,10):
	for reduced_numerator in range(1,reduced_denominator):
	    ratio = Fraction(reduced_numerator,reduced_denominator)
	    for common_factor in range(1,10):
		for numerator,denominator in ((reduced_numerator * 10 + common_factor,
						common_factor * 10 + reduced_denominator),
						(common_factor* 10 + reduced_numerator,
						reduced_denominator * 10 + common_factor)):
		    if Fraction(numerator,denominator) == ratio:
			yield ratio

print reduce(operator.mul,reducible_fractions()).denominator
