#!/usr/bin/env python
# 1533776805
# 0.27 s

from itertools import count, dropwhile
import sys

def triangles():
	for n in count(1):
		yield n * (n + 1) / 2

def pentagons():
	for n in count(1):
		yield n * (3*n - 1) / 2

def hexagons():
	for n in count(1):
		yield n * (2*n - 1)

def trianglepentagonhexagons():
	triang_iter = triangles()
	pentag_iter = pentagons()
	for hexag in hexagons():
		for pentag in dropwhile(lambda p: p < hexag, pentag_iter):
			if pentag == hexag:
				for triang in dropwhile(lambda t: t < hexag,triang_iter):
					if triang == hexag:
						yield hexag
					break
			break

def first_tph_greater_than(n):
	for tph in dropwhile(lambda t:t<=n,trianglepentagonhexagons()):
		return tph

print first_tph_greater_than(sys.argv[1] if sys.argv[1:] else 40755)
