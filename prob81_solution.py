memoized_paths = {}
matrix = []
for index, line in enumerate(open('matrix.txt','r')):
    matrix.append(line.split(','))

memoized_paths[(0,0)] = matrix[0][0]

def minimal_path(x,y):
    if (x,y) in memoized_paths:
        return memoized_paths[(x,y)]
    if x < 0 or y < 0:
        return None
    left = minimal_path(x-1,y)
    up = minimal_path(x,y-1)
    if left and up:
        choice = min(left,up)
    else:
        choice = left or up
    result = choice + matrix[x][y]
    memoized_paths[(x,y)] = result

for x in range(len(matrix)):
    for y in range(len(matrix[i])):
        minimal_path(x,y)

print memoized_paths[(len(matrix)-1,len(matrix[len(matrix)-1]-1))]
