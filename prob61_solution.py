#!/usr/bin/env python
import itertools

def triangles():
    for n in itertools.count(1):
        yield (n * (n + 1))/2

def squares():
    for n in itertools.count(1):
        yield n ** 2

def pentagons():
    for n in itertools.count(1):
        yield n * (3 * n - 1) / 2

def hexagons():
    for n in itertools.count(1):
        yield n * (2 * n - 1)

def heptagons():
    for n in itertools.count(1):
        yield n * (5*n - 3) / 2

def octagons():
    for n in itertools.count(1):
        yield n * (3 * n - 2)

# for an ordered iterable, return a tuple of every element >= 1000 and < 10000
def four_digit_examples(iterable):
    return tuple(itertools.takewhile(lambda x: x < 10000, itertools.dropwhile(lambda x: x < 1000, iterable)))

# the elements of group starting with first_two_digits
def starting_with(first_two_digits, group):
    minimum = first_two_digits * 100
    return filter(lambda x:x >= minimum and x < minimum + 100, group)

# return the first four-digit cycle found
def four_digit_cycle(generators):
    four_digit_lists = map(four_digit_examples,generators)
    smallest_four_digit_list = min(four_digit_lists, key=len)
    other_four_digit_lists = set(four_digit_lists) - set([smallest_four_digit_list])
    for element in smallest_four_digit_list:
        chain = four_digit_chain(element / 100, other_four_digit_lists, element % 100)
        if chain:
            return [element] + chain

# if we can reach final_two_digits by making a chain of
#  elements, one from each of four_digit_lists, such that
#  the last two digits of one are the first two digits of
#  the next, return it; else return None
def four_digit_chain(final_two_digits,four_digit_lists,starting_two_digits):
    # base case - have we reached final_two_digits?
    if len(four_digit_lists) == 0:
        if final_two_digits == starting_two_digits:
            return []
        return None
    # for each list in the set, if an element starts with starting_two_digits,
    #  try recursing over the other lists with the last two digits of that element
    for four_digit_list in four_digit_lists:
        for element in starting_with(starting_two_digits,four_digit_list):
            chain = four_digit_chain(final_two_digits,four_digit_lists - set([four_digit_list]),element % 100)
            if chain is not None:
                return [element] + chain
    return None

print sum(four_digit_cycle([triangles(),squares(),pentagons(),hexagons(),heptagons(),octagons()]))
