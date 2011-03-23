#!/usr/bin/env python

memo_table = {}
color_sizes = [2,3,4]

def num_ways_to_fill(row_size):
    if row_size < 0:
        return 0
    elif row_size < min(color_sizes):
        return 1
    elif row_size in memo_table:
        return memo_table[row_size]
    else:
        no_rightmost_block = num_ways_to_fill(row_size - 1)
        rightmost_block = sum(map(lambda color: num_ways_to_fill(row_size-color), color_sizes))
        total = no_rightmost_block + rightmost_block
        memo_table[row_size] = total
        return total

print num_ways_to_fill(50)
