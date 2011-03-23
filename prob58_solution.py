#!/usr/bin/env python
# 26241
# 8.0s

from itertools import takewhile

prime_list = [3,5,7]
def prime(n):
    def count(init,step):
	while(True):
	    yield init
	    init += step
    if not n % 2 or n == 1:
	return False
    for p in takewhile(lambda x: x * x <= n, prime_list):
	if not n % p:
	    return False
    while prime_list[-1] * prime_list[-1] < n:
	for odd_number in count(prime_list[-1] + 2,2):
	    if prime(odd_number):
		prime_list.append(odd_number)
		if not n % odd_number:
                    return False
		break
    return True

def first_spiral(ratio):
    def spiral():
	corner = 1
	offset = 2
	while(True):
	    for i in range(4):
		    yield corner
		    corner += offset
	    offset += 2
    def squares():
        spiral_iter = spiral()
	yield ((spiral_iter.next(),), 1)
	while(True):
	    corners = tuple(map(lambda _: spiral_iter.next(),range(4)))
	    yield (corners,corners[1]-corners[0] + 1)
    prime_count = 0
    total_count = 0
    for corners, side_length in squares():
	for corner in corners:
	    if prime(corner):
		prime_count += 1
	    total_count += 1
	if prime_count * ratio < total_count and total_count > 1:
	    return side_length

print first_spiral(10)
