#!/usr/bin/env python
from itertools import count

memo_table = {}

def num_ways_to_fill(row_size, minimum_length):
    if row_size < minimum_length:
        return 1
    elif (row_size, minimum_length) in memo_table:
        return memo_table[(row_size,minimum_length)]
    else:
        no_rightmost_block = num_ways_to_fill(row_size - 1, minimum_length)
        rightmost_block = sum(map(lambda x: num_ways_to_fill(row_size - x - 1, minimum_length),range(minimum_length,row_size + 1)))
        total = no_rightmost_block + rightmost_block
        memo_table[(row_size, minimum_length)] = total
        return total

def first_exceeds_one_million(minimum_length):
    for row_size in count(minimum_length):
        if num_ways_to_fill(row_size, minimum_length) > 1000000:
            return row_size

print first_exceeds_one_million(50)
