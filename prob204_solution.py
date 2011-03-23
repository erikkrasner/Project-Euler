def primes_up_to(n):
    primes = []
    for prime in prime_list:
        if prime > n:
            break
        primes.append(prime)
    return primes

def hamming(n, maximum):
    small_primes = primes_up_to(n)
    distincts = set([1])
    hamming_queue = Queue()
    hamming_queue.put(1)
    while not hamming_queue.empty():
        hamming = hamming_queue.get()
        for prime in small_primes:
            new_hamming = hamming * prime
            if new_hamming <= maximum and new_hamming not in distincts:
                distincts.add(new_hamming)
                hamming_queue.put(new_hamming)
    return len(distincts)

print hamming(100,10**9)
