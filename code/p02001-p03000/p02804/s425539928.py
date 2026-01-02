import math
from functools import lru_cache
from operator import mul
from functools import reduce


def resolve():
    import sys
    input = sys.stdin.readline
    MOD = 10**9 + 7
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()
    B = A[::-1]

    @lru_cache(maxsize=None)
    def combinations_count__(n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    @lru_cache(maxsize=None)
    def combinations_count____(n, r):
        r = min(r, n - r)
        numer = reduce(mul, range(n, n - r, -1), 1)
        denom = reduce(mul, range(1, r + 1), 1)
        return numer // denom

    def combinations_count_(n, r):
        if n - r < r: r = n - r
        if r == 0: return 1
        if r == 1: return n

        numerator = [n - r + k + 1 for k in range(r)]
        denominator = [k + 1 for k in range(r)]

        for p in range(2,r+1):
            pivot = denominator[p - 1]
            if pivot > 1:
                offset = (n - r) % p
                for k in range(p-1,r,p):
                    numerator[k - offset] /= pivot
                    denominator[k] /= pivot

        result = 1
        for k in range(r):
            if numerator[k] > 1:
                result *= int(numerator[k])

        return result

    def modinv(a, mod=10**9+7):
        return pow(a, mod-2, mod)

    def combinations_count(n, r, mod=10**9+7):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n-r)
        return fact[n] * factinv[r] * factinv[n-r] % mod
    
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]
    for i in range(2, N + 1):
        fact.append((fact[-1] * i) % MOD)
        inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
        factinv.append((factinv[-1] * inv[-1]) % MOD)

    sum = 0
    for i in range(K-1, N):
        sum += combinations_count(i, K-1) * A[i] % MOD - combinations_count(i, K-1) * B[i] % MOD

    print(sum % MOD)


if __name__ == "__main__":
    resolve()