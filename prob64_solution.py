#!/usr/bin/env python
# 1322
# 1.2 seconds
from itertools import ifilter, imap, ifilterfalse

# Wikipedia'd algorithm for finding the period of root(s) as a
#  continued fraction
def continued_fraction_expansion_period(s):
	a,d,m = int(s**0.5),1,0
	init_a = a
	triple_list = []
	triple_set = set()
	while (a,d,m) not in triple_set:
		triple_list.append((a,d,m))
		triple_set.add((a,d,m))
		next_m = d * a - m
		next_d = (s - (next_m * next_m)) / d
		next_a = (init_a + next_m) / next_d
		a,d,m = next_a, next_d, next_m
	return len(triple_list) - triple_list.index((a,d,m))

#perfect-squareness checker suitable for small integers
def perfect_square(n):
    return (n ** 0.5) % 1 == 0

#itertools-dense function for counting odd periods
def num_odd_periods(n):
	count = 0
	for odd_period in ifilter(lambda x:x%2,
                                  (imap(continued_fraction_expansion_period,
                                        ifilterfalse(perfect_square,xrange(2,n+1))))):
		count += 1
	return count

print num_odd_periods(10000)
