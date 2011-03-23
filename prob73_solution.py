def reduced_proper_fractions():
    reduced_fractions = set()
    for denominator in range(5,12001):
        for numerator in range(denominator / 3, (denominator / 2) + 1):
            frac = Fraction([numerator,denominator])
            frac.reduce()
            if tuple(frac) not in reduced_fractions:
                approximation = 1.0 * frac.numerator()/frac.denominator()
                if approximation > 1.0/3 and approximation < 1.0/2:
                    reduced_fractions.add(tuple(frac))
    return len(reduced_fractions)
