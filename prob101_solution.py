#!/usr/bin/env python

def polynomial(seq):
    def poly(n):
        total = 0
        for power, coefficient in enumerate(seq):
            total += (n**power) * coefficient
        return total
    return poly

def lagrange_polynomial(x_list,y_list):
    def lp(x):
        x_minus = lambda x_i: x - x_i
        total = 0
        for index in range(len(x_list)):
            numerator = product(map(x_minus,x_list[:index]+x_list[index+1:]))
            denominator = product(map(lambda x_i: x_list[index] - x_i,x_list[:index] + x_list[index+1:]))
            total += y_list[index] * numerator / denominator
        return total
    return lp

def sum_first_incorrect_terms(polynomial,degree):
    correct_terms = map(polynomial,range(1,degree+2))
    fit_sum = 0
    for smaller_degree in range(degree):
        approximator = lagrange_polynomial(range(1,smaller_degree+2),correct_terms[:smaller_degree+1])
        next_term = correct_terms[smaller_degree + 1]
        approx_term = approximator(smaller_degree + 2)
        print str(next_term) + " " + str(approx_term)
        if approx_term != next_term:
            fit_sum += approx_term
    return fit_sum

print sum_first_incorrect_terms(polynomial((1,-1,1,-1,1,-1,1,-1,1,-1,1)),10)