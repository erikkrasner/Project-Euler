def split_at(lst, value):
    new_lst = []
    for element in lst:
        if element < value:
            new_lst.append(element)
        else:
            break
    return new_lst
def sum_of_most_primes_less_than(n):
    small_enough_primes = split_at(prime_list,n)
    best_prime = prime_list[0]
    for num_primes in itertools.count(1):
        if sum(small_enough_primes[:num_primes]) > n:
            return best_prime
        sums_of_n_primes = set(map(lambda i: sum(small_enough_primes[i:i+num_primes]), range(len(small_enough_primes) - num_primes)))
        for prime in small_enough_primes:
            if prime in sums_of_n_primes:
                best_prime = prime
                break

sum_of_most_primes_less_than(1000000)
