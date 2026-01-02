from operator import mul
from functools import reduce

N, K = map(int, input().split())
MOD = 10 ** 9 + 7


def comb(N, R):
    R = min(N-R, R)
    if R == 0: return 1
    over = reduce(mul, range(N, N - R, -1))
    under = reduce(mul, range(1,R + 1))
    return over // under % MOD


def f2(N, K):
    return comb(N+K-1, K-1)

def f(N, K):
    if (N < K): return 0
    if N == 0 and K == 0: return 1
    if (K < 1): return 0
    return f2(N-K, K)


for i in range(1,K+1):
    blue = f(K, i)
    red = 0
    red += f(N-K, i-1)
    red += f(N-K, i) * 2 % MOD
    red += f(N-K, i+1) % MOD
    
    print(red * blue % MOD)