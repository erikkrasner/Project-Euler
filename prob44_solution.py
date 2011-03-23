def pentagonals(start,end):
	for n in itertools.count((1 + (1 +24*start)**0.5)/6):
		nth_pentagonal = n * (3 * n - 1) / 2
		if nth_pentagonal > end:
			break
		if nth_pentagonal >= start:
			yield nth_pentagonal

def is_pentagonal(num):
	return ((1 + (1 +24*num)**0.5)/6) % 1.0 == 0

def pentagonal_difference():
	counter = 1
	for d in pentagonals(1,10000000):
		if counter % 100 == 0:
			print counter
		for p_j in pentagonals(1,d):
			p_k = p_j + d
			if is_pentagonal(p_k) and is_pentagonal(p_j + p_k):
				print p_j
				print p_k
				return d
		counter += 1

