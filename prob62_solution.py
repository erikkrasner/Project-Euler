#! /usr/bin/env python
from itertools import count

def cubes():
    for n in count(1):
        yield n**3

digit_tags = {}
def smallest_cube(num_permutations):
    for cube in cubes():
        digit_tag = tuple(sorted(str(cube)))
        if digit_tag in digit_tags:
            new_total = digit_tags[digit_tag][0] + 1
            smallest_cube_list = digit_tags[digit_tag][1]
            if new_total == num_permutations:
                return smallest_cube_list[0]
            digit_tags[digit_tag] = (new_total,smallest_cube_list)
            smallest_cube_list += [cube]
        else:
            digit_tags[digit_tag] = (1,[cube])

print smallest_cube(5)
