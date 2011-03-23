def pythagorean_triple_with_most_solutions(max_perimeter):
    perimeters_to_triples = {}
    for n in range(1,max_perimeter):
        for m in range(n+1,max_perimeter):
            py_trip = (m**2 - n**2, 2*m*n, m**2 + n**2)
    perimeter = sum(py_trip)
    coefficient = 1
    while perimeter <= max_perimeter:
        new_py_trip = map(lambda x: x * coefficient, py_trip)
        new_py_trip.sort()
        perimeter = sum(new_py_trip)
        if perimeter not in perimeters_to_triples:
            perimeters_to_triples[perimeter] = set()
        perimeters_to_triples[perimeter].add(tuple(new_py_trip))
        coefficient += 1
        return max(perimeters_to_triples.values(), key=len)
