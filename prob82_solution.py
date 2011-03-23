def best_paths():
    def best_path_to(column,row):
        if (column,row) in paths:
            return paths[(column,row)]
        best_path = min(map(lambda alt_row: best_path_to(column - 1,alt_row) + sum(matrix[column][alt_row:row:1 if row>alt_row else -1]) + matrix[column][row],range(80)))
        paths[(column,row)] = best_path
    paths = {}
    for row, value in enumerate(matrix[0]):
        paths[(0,row)] = value
        for column in range(1,80):
            print column
            for row in range(80):
                best_path_to(column,row)
    return min(map(lambda row:best_path_to(79,row),range(79)))
