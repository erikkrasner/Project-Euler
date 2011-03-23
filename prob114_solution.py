#!/usr/bin/env python
memo_table = {}

def num_ways_to_fill(row_size):
    if row_size < 3:
        return 1
    elif row_size in memo_table:
        return memo_table[row_size]
    else:
        # number of solutions with no block in the rightmost position,
        #  find recursively
        no_rightmost_block = num_ways_to_fill(row_size - 1)
        # for block size 3 to row_size in the rightmost position,
        #  number of solutions is the number of ways to arrange blocks
        #  separated by at least one square from the rightmost block
        rightmost_block = sum(map(lambda x: num_ways_to_fill(row_size - x - 1),range(3,row_size + 1)))
        total = no_rightmost_block + rightmost_block
        memo_table[row_size] = total
        return total

print num_ways_to_fill(50)
