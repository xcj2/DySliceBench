# D - Factorization

import math, collections

N, M = map(int, input().split())
MOD = 10**9 + 7

# n以下の全ての素数のセットを返す関数
def prime_set(n):
    primes = set(range(2, n+1))
    for i in range(2, int(n**0.5) + 1):
        primes.difference_update(range(i*2, n+1, i))
    return primes

# nを素因数分解して素因数の全リストを返す関数
def prime_factors_duplicating_list(n):
    f = []
    for i in prime_set(int(n**0.5) + 1):
        while n % i == 0:
            f.append(i)
            n //= i
    if n > 1:
        f.append(n)
    return f

def comb(n, r):
    if n < r:
        return 0
    else:
        tmp, tmp2 = 1, n
        for _ in range(r):
            tmp *= tmp2
            tmp2 -= 1
        return tmp // math.factorial(r)
    
M_pf_dict = collections.Counter(prime_factors_duplicating_list(M))

ans = 1
for value in M_pf_dict.values():
    ans *= comb(N-1+value, value)
    ans %= MOD

print(ans)