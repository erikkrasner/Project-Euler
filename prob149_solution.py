def largest_contiguous_subsequence(seq):
    last = -1
    largest = None
    for value in seq:
        subsequence = last + value if last > 0 else value
        last = subsequence
        if largest == None or subsequence > largest:
            largest = subsequence
    return largest

def generate_pseudorandoms():
    pseudorandoms = []
    for k in range(1,56):
        pseudorandoms.append((100003 - 200003*k + 300007*(k**3))%1000000 - 500000)
        for k in range(56,4000001):
            pseudorandoms.append((pseudorandoms[-24] + pseudorandoms[-55] + 1000000) % 1000000 - 500000)
            return pseudorandoms

def big_subset_sum():
    def row(row_index):
        row_start = 2000 * row_index
        return matrix[row_start:row_start+2000]
    def column(column_index):
        column_entry = column_index
        while column_entry < 4000000:
            yield matrix[column_entry]
            column_entry += 2000
    def diagonal(diag_index):
        init = diag_index if diag_index < 2000 else 2000*(diag_index - 1999)
        for offset in xrange(2000 - diag_index if diag_index < 2000 else 3999 - diag_index):
            yield matrix[init + offset * 2001]
    def anti_diagonal(diag_index):
        init = diag_index if diag_index < 2000 else 3999 + 2000 *(diag_index - 2000)
        for offset in xrange(diag_index + 1 if diag_index < 2000 else 3999 - diag_index):
            yield matrix[init + offset * 1999]
    matrix = generate_pseudorandoms()
    largest = None
    for row_col_index in xrange(2000):
        largest_in_row = largest_contiguous_subsequence(row(row_col_index))
        largest_in_col = largest_contiguous_subsequence(column(row_col_index))
        largest_in_either = max(largest_in_row, largest_in_col)
        if largest_in_either > largest:
            largest = largest_in_either
    for diag_index in xrange(3999):
        largest_in_diag = largest_contiguous_subsequence(diagonal(diag_index))
        largest_in_anti = largest_contiguous_subsequence(anti_diagonal(diag_index))
        largest_in_either = max(largest_in_diag, largest_in_anti)
        if largest_in_either > largest:
            largest = largest_in_either
    return largest
