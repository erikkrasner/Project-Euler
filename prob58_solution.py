#!/usr/bin/env python
# 26241
# 15.45 s

from itertools import takewhile
from prime_gen import *

def first_spiral(ratio):
    def spiral():
	corner = 1
	offset = 2
	while(True):
	    for _ in range(4):
		yield corner
		corner += offset
	    offset += 2
    def squares():
        spiral_iter = spiral()
	yield ((spiral_iter.next(),), 1)
	while(True):
	    corners = (next(spiral_iter),next(spiral_iter),next(spiral_iter),next(spiral_iter))
	    yield (corners,corners[1]-corners[0] + 1)
    prime_count = 0
    total_count = 0
    for corners, side_length in squares():
	for corner in corners:
	    if prime(corner):
		prime_count += 1
	total_count += len(corners)
	if prime_count * ratio < total_count and total_count > 1:
	    return side_length

print first_spiral(10)
