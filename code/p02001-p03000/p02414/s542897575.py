def input_mat(r, c):
    mat = []
    for _ in range(r):
        row = [int(s) for s in input().split()]
        assert len(row) == c
        mat.append(row)
    return mat

def mat_prod(A, B, n, m, l):
    mat = []
    for i in range(n):
        row = []
        for j in range(l):
            v = sum((A[i][x] * B[x][j] for x in range(m)))
            row.append(v)
        mat.append(row)
    return mat

def print_mat(mat):
    for r in mat:
        print(" ".join(map(str, r)))

if __name__ == '__main__':
    n, m, l = [int(s) for s in input().split()]
    A = input_mat(n, m)
    B = input_mat(m, l)
    #T = [[2,3],[1,4]]
    #E = [[1,0],[0,1]]
    #print_mat((mat_prod(T, E, 2, 2, 2)))
    C = mat_prod(A, B, n, m, l)
    print_mat(C)

