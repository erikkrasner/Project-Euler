memo_table76 = {}

def ways_to_write_as_sum(n,up_to):
    if (n,up_to) in memo_table76:
        return memo_table76[(n,up_to)]
    if n <= 0 or up_to ==0:
        return 0
    result = ways_to_write_as_sum(n - up_to,up_to) + ways_to_write_as_sum(n, up_to - 1)
    if up_to == n:
        result += 1
        memo_table76[(n,up_to)] = result
        return result

for n in range(1,101):
    for up_to in range(1,n+1):
        ways_to_write_as_sum(n,up_to)

print ways_to_write_as_sum(100,99)
