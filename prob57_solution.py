def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a

class Fraction():
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
    def reduce(self):
        common = gcd(self.numerator,self.denominator)
        return Fraction(self.numerator / common, self.denominator / common)
    def plus(self,fraction):
        new_numerator = self.numerator * fraction.denominator + fraction.numerator * self.denominator
        new_denominator = self.denominator * fraction.denominator
        return Fraction(new_numerator,new_denominator).reduce()
    def times(self,fraction):
        new_numerator = self.numerator * fraction.numerator
        new_denominator = self.denominator * fraction.denominator
        return Fraction(new_numerator,new_denominator).reduce()
    def divide_by(self,fraction):
        return self.times(fraction.inverse())
    def inverse(self):
        return Fraction(self.denominator,self.numerator)

def root_two_expansions(n):
    fractional_part = Fraction(1,2)
    one = Fraction(1,1)
    two = Fraction(2,1)
    for iteration in range(n):
        yield fractional_part.plus(one)
        fractional_part = fractional_part.plus(two).inverse()

len(filter(lambda x: len(str(x.numerator)) > len(str(x.denominator)),root_two_expansions(1000)))
