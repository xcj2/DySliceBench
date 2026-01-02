def initSquare(H, W):
    square = []
    for r in range(H):
        row = []
        row_string = input()
        for letter in row_string:
            row.append(letter)
        square.append(row)
    return square

def rowChecker(square):
    delete_row_indexes = []
    for i, row in enumerate(square):
        if "#" not in row:
            delete_row_indexes.append(i)            
    return delete_row_indexes

def columnChecker(square):
    delete_column_indexes = []
    for c in range(W):
        column = []
        for r in range(H):
            column.append(square[r][c])
        if "#" not in column:
            delete_column_indexes.append(c)            
    return delete_column_indexes

def generateNewSquare(square, delete_row_indexes,delete_column_indexes):
    new_square = []
    for r, row in enumerate(square):
        if r not in delete_row_indexes:
            new_row = []
            for c, column in enumerate(row):
                if c not in delete_column_indexes:
                    new_row.append(column)
            new_square.append(new_row)
    return new_square

H, W = [int(i) for i in input().split()]

square = initSquare(H, W)
delete_row_indexes = rowChecker(square)
delete_column_indexes = columnChecker(square)
new_square = generateNewSquare(square, delete_row_indexes,delete_column_indexes)

for row in new_square:
    row_string = ''.join(row)
    print(row_string)