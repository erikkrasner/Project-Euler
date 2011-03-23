#note - took like five hours
def min_subtriangle_sum(triangle_array):
    min_sum = float("Infinity")
    for row_index in range(len(triangle_array)):
        if row_index % 10 == 0:
            print row_index
        for column_index in range(row_index+1):
            current_sum = 0
            for row_offset, last_row in enumerate(triangle_array[row_index:]):
                current_sum += sum(last_row[column_index:column_index + row_offset + 1])
                if current_sum < min_sum:
                    min_sum = current_sum
    return min_sum

def min_subtriangle_sum_problem():
    generator = lcg()
    triangle = []
    for i in xrange(1,1001):
        triangle.append(map(lambda _:generator.next(),xrange(i)))
    print "triangle built"
    return min_subtriangle_sum(triangle)
