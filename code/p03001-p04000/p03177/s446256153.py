import sys

stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


def matrix_cal(A, B, mod):
    a = len(A)
    b = len(A[0])
    c = len(B)
    d = len(B[0])

    assert(b == c)
    ans = [[0] * d for _ in range(a)]
    for aa in range(a):
        for dd in range(d):
            v = 0
            for bb in range(b):
                v = (v + A[aa][bb] * B[bb][dd]) % mod
            ans[aa][dd] = v
    return ans


def matrix_pow(A, n, mod=0):
    if n == 1:
        return A
    a = matrix_pow(A, n//2, mod)
    ans = matrix_cal(a, a, mod)
    if n % 2 == 1:
        ans = matrix_cal(ans, A, mod)
    return ans


N, K = na()
A = naa(N)
mod = 10 ** 9 + 7

B = matrix_pow(A, K, mod)

ans = 0
for i in range(N):
    for j in range(N):
        ans = (ans + B[i][j]) % mod


print(ans)
