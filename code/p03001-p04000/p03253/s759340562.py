from collections import defaultdict

#素因数分解O(√n)
def primeFactor(n):
    res = defaultdict(lambda: 0)
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            res[i] += 1
            n = n // i
    if n != 1:
        res[n] = 1
    return res

import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

#重複組み合わせ
def combinations_with_replacement_count(n, r):
    return combinations_count(n + r - 1, r)

N, M = map(int, input().split())
mod = 10 ** 9 + 7

factors = primeFactor(M)

ans = 1
for v in factors.values():
    ans *= combinations_with_replacement_count(N, v)
    ans %= mod

print(ans)

