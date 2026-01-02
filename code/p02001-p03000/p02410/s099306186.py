def get_matrix_size(x):
    row = len(x)
    col = len(x[0])
    return row, col

def get_matrix(x):
    row, col = get_matrix_size(x)
    for i in range(row):
        line = list(map(int, input().split()))
        if len(line) != col:
            break
        x[i] = line

def get_matrix_product(a, b):
    a_row, a_col = get_matrix_size(a)
    b_row, b_col = get_matrix_size(b)
    if a_col != b_row:
        return
    c_row = a_row
    c_col = b_col
    c = [[0 for j in range(c_col)] for i in range(c_row)]
    for i in range(c_row):
        for j in range(c_col):
            for k in range(a_col):
                c[i][j] += a[i][k] * b[k][j]    
    return c

n, m = map(int, input().split())
a = [[0 for j in range(m)] for i in range(n)]
b = [[0 for j in range(1)] for i in range(m)]
get_matrix(a)
get_matrix(b)
c = get_matrix_product(a, b)
for i in range(len(c)):
    print(c[i][0])

