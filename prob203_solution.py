prime_file = open('primes1.txt','r')
prime_list = []
for line in prime_file:
    prime_list += map(int,line.split())

def pascal_row(last_pascal_row):
    pascal_row = [last_pascal_row[0]]
    for index in range(1,len(last_pascal_row)):
        pascal_row.append(last_pascal_row[index-1] + last_pascal_row[index])
    pascal_row.append(last_pascal_row[-1])
    return pascal_row

def squarefree(n):
    for prime in prime_list:
        square = prime ** 2
        if square > n:
            return True
        if n % square == 0:
            return False

def sum_pascal_rows():
    distincts = set()
    p_row = [1]
    for row in range(50):
        p_row = pascal_row(p_row)
        for element in p_row:
            if element not in distincts and squarefree(element):
                distincts.add(element)
    return sum(distincts)

print sum_pascal_rows()
