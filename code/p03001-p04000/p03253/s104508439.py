#!/usr/bin/env python3

from collections import defaultdict

MOD = 1000000007
fact = []

def main():
    init_fact(2 * 10 ** 5)
    n, m = map(int, input().split())
    pf = prime_factor(m)
    cnt = defaultdict(int)
    for x in pf:
        cnt[x] += 1
    res = 1
    for k, v in cnt.items():
        res *= combi(n - 1 + v, v)
        res %= MOD
    print(res)

def combi(n, k):
    numera = fact[n]
    denomi = (fact[n - k] * fact[k]) % MOD
    return (numera * inv(denomi)) % MOD

def init_fact(maxn):
    assert len(fact) == 0
    fact.append(1)
    for i in range(1, maxn + 1):
        fact.append((fact[i - 1] * i) % MOD)

def inv(n):
    return pow(n, MOD - 2)

def pow(n, p):
    if p == 0:
        return 1
    elif p % 2 == 0:
        x = pow(n, p // 2)
        return (x * x) % MOD
    else:
        x = pow(n, p - 1)
        return (x * n) % MOD

def prime_factor(n):
    # n の素因数を重複有りの昇順リストで返す。O(sqrt n)
    resid = n
    result = []
    i = 2
    while True:
        if resid <= 1:
            return result
        if i ** 2 > resid:
            result.append(resid)
            return result
        if resid % i == 0:
            result.append(i)
            resid //= i
        else:
            i += 1

if __name__ == "__main__":
    main()
