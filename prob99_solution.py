import math
best_index = 0
best_pair = (1,0)
def a_to_b_greater_than_c_to_d(a,b,c,d):
    return b * math.log(a) > d * math.log(c)
for index, line in enumerate(open('base_exp.txt','r')):
    base, exp = map(int,line.split(','))
    if a_to_b_greater_than_c_to_d(base,exp,best_pair[0],best_pair[1]):
        best_index = index + 1
        best_pair = (base,exp)
print best_index
