#!/usr/bin/env python
# 1074 for problem 18
# 7273 for problem 67
# 0.112 s

triangle_string = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

def maximum_total(triangle):
    total_memo = {}
    def maximum_total_helper(row,column):
	if column < 0 or column > row:
	    return 0
	if (row,column) in total_memo:
	    return total_memo[row,column]
	best_total = triangle[row][column] + max((maximum_total_helper(row-1,column-1),
						    maximum_total_helper(row-1,column)))
	total_memo[row,column] = best_total
	return best_total
    return max([maximum_total_helper(len(triangle)-1,column)
		    for column in range(len(triangle))])

print "problem 18:", maximum_total([map(int,row.split())
                                 for row in triangle_string.split('\n')])

print "problem 67:", maximum_total([map(int,row.split())
                                    for row in open('triangle.txt','r')])
