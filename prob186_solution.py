#!/usr/bin/env python
# 2325629
# 59.977 s, hey I'll take it

# Lagged Fibonacci generator
def lfg():
    sks = [(100003 - 200003*k + 300007 * k**3) % 1000000 for k in range(1,56)]
    for sk in sks: yield sk
    while True:
	sks.append((sks[-24] + sks[-55]) % 1000000)
	yield sks[-1]
	# 1000 chosen experimentally so sks doesn't eat
	#  all the memory but isn't constantly realloced
	if len(sks) >= 10000:
	    sks = sks[-55:]

# Return results from the lagged Fibonacci generator in pairs.
def calls():
    numbers = lfg()
    while True:
	yield (numbers.next(),numbers.next())

# parent and rank keep track of parents and ranks per standard
#  union-find usage. size[n] is the size of the disjoint set
#  rooted at n.
parent,rank,size = {},{},{}

#initialize a disjoint set of one member, rank 0
def makeset(x):
    parent[x] = x
    rank[x] = 0
    size[x] = 1

#union two disjoint sets into one
def union(x,y):
    def setparent(newchild,newparent):
	parent[newchild] = newparent
	size[newparent] = size[newparent] + size[newchild]
    rx,ry = find(x),find(y)
    if rx != ry:
	if rank[rx] > rank[ry]:
	    setparent(ry,rx)
	else:
	    setparent(rx,ry)
	    if rank[rx] == rank[ry]:
		rank[ry] = rank[ry] + 1

#find the root of a disjoint set
def find(x):
    if x != parent[x]:
	parent[x] = find(parent[x])
    return parent[x]

def when_does_prime_minister_have_enough_friends():
    PRIME_MINISTER = 524287
    count = 0
    prime_minister_found = False
    for caller, callee in calls():
	if caller != callee:
	    for number in (caller, callee):
		if number not in parent:
		    makeset(number)
	    count += 1
	    if (not prime_minister_found) and PRIME_MINISTER in (caller, callee):
		prime_minister_found = True
	    union(caller,callee)
	    if prime_minister_found and size[find(PRIME_MINISTER)] >= 990000:
		return count

print when_does_prime_minister_have_enough_friends()
