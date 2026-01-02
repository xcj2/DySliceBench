import math
import sys

sys.setrecursionlimit(10000)
INF = float('inf')


def inv(x):
    return pow(x, MOD - 2, MOD)


def comb(n, r, mod):
    # https://fushime2.hatenablog.com/entry/2016/11/12/155543
    return (math.factorial(n) * inv(math.factorial(n - r)) * inv(math.factorial(r))) % mod


N, M, K = list(map(int, input().split()))


def pyramid(n):
    return n * (n + 1) * (n + 2) // 6


MOD = 10 ** 9 + 7

# K ==2 の場合
# print(pyramid(N - 1) * M ** 2 + pyramid(M - 1) * N ** 2)
k2 = (pyramid(N - 1) * M ** 2 + pyramid(M - 1) * N ** 2) % MOD
# k2 を何回使うか
c = comb(N * M - 2, K - 2, mod=MOD)
print(k2 * c % MOD)
