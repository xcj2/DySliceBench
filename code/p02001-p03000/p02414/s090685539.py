def ext_row(i, matrix):
    return matrix[i]


def ext_col(j, matrix):
    return [row[j] for row in matrix]


def inner_prod(va, vb):
    return sum([a * b for a, b in zip(va, vb)])


n, m, l = map(int, input().split())

A = [[0] * m for _ in range(n)]
B = [[0] * l for _ in range(m)]

for i in range(n):
    A[i] = [int(c) for c in input().split()]
for i in range(m):
    B[i] = [int(c) for c in input().split()]

ans = [[0] * l for _ in range(n)]
for i in range(n):
    for j in range(l):
        ans[i][j] = inner_prod(ext_row(i, A), ext_col(j, B))
for row in ans:
    print(' '.join([str(i) for i in row]))

