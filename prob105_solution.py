import itertools

def disjoint(set1,set2):
    return not set1.intersection(set2)

def is_special_sum_set(the_set):
    subsets = []
    for length in range(len(the_set)):
        for subset in itertools.combinations(the_set,length):
            disjoint_subsets = filter(lambda s:disjoint(s,subset),subsets)
            subset_sum = sum(subset)
            for disjoint_subset in disjoint_subsets:
                alt_subset_sum = sum(disjoint_subset)
                if alt_subset_sum == subset_sum or (len(disjoint_subset) < len(subset) and alt_subset_sum > subset_sum):
                    return False
            subsets.append(set(subset))
    return True

def sets():
    for line in open('/Users/Erik/Documents/code/proj_euler/sets.txt','r'):
        yield set(map(int,line.split(',')))

sum(map(sum,filter(is_special_sum_set,sets())))
