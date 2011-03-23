#!/usr/bin/env python

memo_table = {}

def num_ways_to_fill(row_size,color_sizes):
    return sum(map(lambda color: num_ways_to_fill_with_color(row_size,color),color_sizes))

def num_ways_to_fill_with_color(row_size,color):
    if row_size < color:
        return 0
    elif (row_size, color) in memo_table:
        return memo_table[(row_size, color)]
    else:
        no_rightmost_block = num_ways_to_fill_with_color(row_size-1,color)
        rightmost_block = num_ways_to_fill_with_color(row_size - color, color) + 1
        total = no_rightmost_block + rightmost_block
        memo_table[(row_size, color)] = total
        return total

print num_ways_to_fill(50,[2,3,4])
