def removeRow(matrix):
    _matrix = []
    for i in range(len(matrix)):
        if max(matrix[i]) == 1:
            _matrix.append(matrix[i])
    return _matrix

def removeCol(matrix):
    r = len(matrix)
    c = len(matrix[0])
    rightRotatedMatrix = []
    for i in range(c):
        col = []
        for j in range(r-1, -1, -1):
            col.append(matrix[j][i])
        rightRotatedMatrix.append(col)    
    rightRotatedMatrix = removeRow(rightRotatedMatrix)
    r = len(rightRotatedMatrix)
    c = len(rightRotatedMatrix[0])
    matrix = []
    for i in range(c-1, -1, -1):
        row = []
        for j in range(r):
            row.append(rightRotatedMatrix[j][i])
        matrix.append(row)
    return matrix

def answer(matrix):
    matrix = removeRow(matrix)
    return removeCol(matrix)

r, c = map(int, input().split())
matrix = []
for _ in range(r):
    row = [i for i in input()]
    for i in range(len(row)):
        if row[i] == '#':
            row[i] = 1
        if row[i] == '.':
            row[i] = 0
    matrix.append(row)
    
matrix = answer(matrix)
for i in range(len(matrix)):
    row = []
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            row.append('#')
        else:
            row.append('.')
    print("".join(row))
        