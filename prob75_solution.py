#!/usr/bin/env python
# 161667
# 
from itertools import count

# Euclid's formula, which is guaranteed to return all primitive
#  Pythagorean triples. Longest_wire is the longest a + b + c
#  such that a, b and c form a pythagorean triple.
#  m ** 2 + 2 * m + 1 is a lower bound on a + b + c =
#  (m ** 2 + n ** 2) + 2 * m * n * (m**2 - n**2).
#  When the lower bound exceeds longest_wire, all subsequent sums
#  must exceed longest_wire.
def euclid_formula(longest_wire):
	for m in count(1):
		if m * m + 2 * m + 1 > longest_wire:
			break
		for n in count(1):
			if n >= m:
				break
			triple = (m * m - n * n, 2 * m * n, m * m + n * n)
			if sum(triple) <= longest_wire:
				yield triple

# An extension of Euclid's formula, guaranteed to yield all
#  Pythagorean triples of wire length up to longest_wire (not
#  uniquely).
def all_triples(longest_wire):
        def tuple_sum(tuple1, tuple2):
            return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1], tuple1[2] + tuple2[2])
	for triple in euclid_formula(longest_wire):
                new_triple = triple
		while sum(new_triple) <= longest_wire:
                        yield new_triple
			new_triple = tuple_sum(new_triple, triple)

# Counts the number of wire lengths corresponding to only
#  one triple. Maintains a hash table mapping all wire lengths
#  previously found to a set of all triples with that wire length.
#  Counts all wire lenghs whose corresponding set has length 1.
def num_wire_lengths_with_unique_triples(longest_wire):
	triples = {}
	for triple in all_triples(longest_wire):
		length = sum(triple)
		triple = tuple(sorted(triple))
		if length not in triples:
			triples[length] = set()
		triples[length].add(triple)
	return len(filter(lambda x: len(triples[x]) == 1, triples))

print num_wire_lengths_with_unique_triples(1500000)
