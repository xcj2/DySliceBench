from math import factorial

MOD = 10 ** 9 + 7

N, K = map(int, input().split())

f = {}
def fact(x):
    if x in f:
        return f[x]
    ans = factorial(x)
    f[x] = ans
    return ans

F = {}
def fact_power(a, b):
    if (a, b) in F:
        return F[(a, b)]
    if b == 0:
        ans = 1
    elif b % 2 == 0:
        d = fact_power(a, b // 2)
        ans = (d * d) % MOD
    else:
        ans = (fact(a) * fact_power(a, b - 1)) % MOD
    F[(a, b)] = ans
    return ans

P = {}
def perm(a, b):
    if b == 0 or a < b:
        return 0
    if (a, b) in P:
        return P[(a, b)]
    ans = fact_power(a - 1, 1) * fact_power(a - b, MOD - 2) * fact_power(b - 1, MOD - 2) % MOD
    P[(a, b)] = ans
    return ans

if N == K:
    print(1)
    for i in range(K - 1):
        print(0)
else:
    for i in range(1, K + 1):
        B = perm(K, i)
        R = perm(N - K, i - 1) + perm(N - K, i) * 2 + perm(N - K, i + 1)
        print(B * R % MOD)
