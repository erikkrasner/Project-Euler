def rad(n):
    prime_factors = [1]
    for prime in ordered_primes:
        if prime ** 2 > n:
            break
        if n % prime == 0:
            prime_factors.append(prime)
            while n % prime == 0:
                n /= prime
    if n in unordered_primes:
        prime_factors.append(n)
    return reduce(lambda a,b:a*b,prime_factors)

sorted(map(lambda n: (n,rad(n)),range(1,100001)),key=lambda pair: pair[1])[9999]
