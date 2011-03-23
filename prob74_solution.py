import math
def digit_fact_sum(n):
    return sum(map(math.factorial,map(int,str(n))))
def sixty_factorial_chains():
    lengths = {}
    for n in [1,2,145,40585]:
        lengths[n] = 1
    for n in [871,872,45361,45362]:
        lengths[n] = 2
    for n in [169,1454,363601]:
        lengths[n] = 3
    for n in xrange(1000000):
        chain = []
        while n not in lengths:
            chain.append(n)
            n = digit_fact_sum(n)
        for index,n2 in enumerate(chain[len(chain)::-1]):
            lengths[n2] = lengths[n] + index + 1
    return len(filter(lambda n: n < 1000000 and lengths[n] == 60,lengths.keys()))
print sixty_factorial_chains()
