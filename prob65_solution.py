def continued_fraction_terms():
    k = 1
    while(True):
        yield Fraction(1,1)
        yield Fraction(2*k,1)
        yield Fraction(1,1)
        k += 1

def convergents_for_e():
    yield Fraction(2,1)
    n_terms = []
    terms = continued_fraction_terms()
    for term in terms:
        n_terms.append(term)
        fractional_part = Fraction(0,1)
        for term in n_terms[::-1]:
            fractional_part = term.plus(fractional_part).inverse()
        yield Fraction(2,1).plus(fractional_part)

for i in range(100):
    convergent = convergents.next()

print sum(map(int,str(convergent.numerator)))
