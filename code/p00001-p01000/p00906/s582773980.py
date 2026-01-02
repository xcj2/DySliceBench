from operator import mul
def dot(v1, v2):
    return sum(map(mul, v1, v2))

def mat_mul(A, B, m):
    tB = tuple(zip(*B))
    return [[dot(A_i, B_j) % m for B_j in tB] for A_i in A]

def mat_pow(X, n, m):
    s = len(X)
    A = [[0] * s for i in range(s)]
    for i in range(s):
        A[i][i] = 1
    
    while n > 0:
        if n & 1:
            A = mat_mul(A, X, m)
        X = mat_mul(X, X, m)
        n >>= 1
    return A

def solve():
    from sys import stdin
    file_input = stdin
    while True:
        N, M, A, B, C, T = map(int, file_input.readline().split())
        if N == 0:
            break
        s = [list(map(int, file_input.readline().split()))]
        
        X = [[0] * N for i in range(N)]
        X[0][0] = B
        X[0][1] = A
        for i, X_i in enumerate(X[1:N-1], start=1):
            X_i[i - 1] = C
            X_i[i] = B
            X_i[i + 1] = A
        X[-1][-2] = C
        X[-1][-1] = B
        
        ans = mat_mul(s, mat_pow(X, T, M), M)
        print(*ans[0])

solve()
