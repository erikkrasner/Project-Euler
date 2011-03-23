#the answer is 5777
def smallest_odd_composite():
	for number in xrange(9,4999999,2):
		if number-1 % 100000 == 0:
			print number
		if number not in prime_set:
			condition = True
			for prime in primes_under_two_mil:
				if prime > number:
					break
				difference = number - prime
				if difference % 2 == 0:
					if ((difference /2)** 0.5)%1.0 == 0:
						condition = False
						break
			if condition:
				return number
