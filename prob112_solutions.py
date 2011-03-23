import itertools

def ninetynine_percent_bouncies():
    num_bouncies = 0
    num_nonbouncies = 0
    for upper_bound in itertools.count(1):
        if upper_bound % 10000 == 0:
            print upper_bound
        if bouncy(upper_bound):
            num_bouncies += 1
        else:
            num_nonbouncies += 1
        if num_nonbouncies * 99 <= num_bouncies:
            return upper_bound

print ninetynine_percent_bouncies()
