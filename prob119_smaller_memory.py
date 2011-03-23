def perfect_powers_in_order(smallest_base):
	def powers_of(base):
		power = base * base
		while(True):
			yield power
			power *= base
	power_iterators = {smallest_base:powers_of(smallest_base)}
	def power_iterator(base):
		return power_iterators[base]
	max_base = smallest_base
	powers = [(power_iterator(smallest_base).next(),smallest_base)]
	max_powers = {}
	def max_power(base):
		if base in max_powers:
			return max_powers[base]
		else:
			power = 12 * (10 ** (base - 1))
			max_powers[base] = power
			return power
	while(True):
		power, base = heapq.heappop(powers)
		yield (power, base)
		if power < max_power(base):
			heapq.heappush(powers,(power_iterator(base).next(),base))
		else:
			max_powers.pop(base)
			power_iterators.pop(base)
		if base == max_base:
			max_base += 1
			power_iterators[max_base] = powers_of(max_base)
			heapq.heappush(powers,(power_iterator(max_base).next(),max_base))
