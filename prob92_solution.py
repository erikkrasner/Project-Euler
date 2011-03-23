memo_hash = {1:False,89:True}
def chains_to_89(n):
    things_to_memoize = []
    while(n not in memo_hash):
        things_to_memoize.append(n)
        n = sum(map(lambda chr:int(chr)**2,str(n)))
    result = memo_hash[n]
    for number in things_to_memoize:
        memo_hash[number] = result
    return result
