#!/usr/bin/env python3

# import sys
# sys.setrecursionlimit(200000)  # ttk

MOD = 1000000007
fact = []
q = []

def main():
    n = int(input())
    an = list(map(int, input().split()))
    init_fact(100000)
    init_q(100000, n)
    res = 0
    for j, a in enumerate(an):
        res += a * (q[n - j] + q[j + 1] - q[1])
        res %= MOD
    print(res)

def init_q(maxn, n):
    assert len(q) == 0
    assert len(fact) == maxn + 1
    q.append(0)
    for l in range(1, maxn + 1):
        dq = fact[n] * inv(l)
        q.append((q[-1] + dq) % MOD)

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

main()
