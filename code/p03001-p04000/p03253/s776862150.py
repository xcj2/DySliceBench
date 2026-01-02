from collections import defaultdict

def sieve_of_eratosthenes(n):
    sr_n = int(n ** 0.5)
    f = [True] * (sr_n + 1)
    res = []
    for i in range(2, sr_n+1):
        if f[i]:
            res.append(i)
            for j in range(2*i, sr_n+1, i):
                f[j] = False
    return res

def trial_division(n):
    pn = sieve_of_eratosthenes(n)
    res = defaultdict(lambda: 0)
    for p in pn:
        while n % p == 0:
            res[p] += 1
            n //= p
    if n > 1:
        res[n] += 1
    return res

def nCr(n, r):
    r = min(r, n-r)
    fact = 1
    inv = 1
    for i in range(r):
        fact *= (n - i)
        fact %= MOD
        inv *= (i + 1)
        inv %= MOD
    return fact * pow(inv, MOD-2, MOD) % MOD

MOD = 10 ** 9 + 7
N, M = map(int, input().split())
n_pf = trial_division(M).values()
ans = 1
for r in n_pf:
    ans *= nCr(N-1+r, r)
    ans %= MOD
print(ans)