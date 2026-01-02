#!/usr/bin/env python3
import sys, os
try: from typing import Any, Union, List, Tuple, Dict
except ImportError: pass
sys.setrecursionlimit(10**6)
if os.environ.get("USER") == "shun":
    def debug(*args): print(*args, file=sys.stderr)
else:
    print("NO DEBUG", file=sys.stderr)
    def debug(*args): pass
def exit(): sys.exit(0)


n, m = map(int, input().split())

p = 10**9 + 7
# 素因数分解
def prime_factorization(n):
    factors = {}
    q = 2
    while n != 1:
        if q**2 > n:
            factors[n] = 1
            break
        while n % q == 0:
            n = n // q
            if q in factors:
                factors[q] += 1
            else:
                factors[q] = 1
        q += 1
    return factors


def power(n, e):
    # debug(".")
    if e == 0:
        return 1
    if e % 2 == 0:
        return power(n**2%p, e//2) % p
    return n * power(n, e-1) % p


def inv(n):
    return power(n, p-2)


# def comb(a, b):
#     if a < b:
#         a, b = b, a
#     assert a >= b
#     res = 1
#     for i in range(a+1, a+b+1):
#         res = (res * i) % p
#     for i in range(1, b+1):
#         res = (res * inv(i)) % p
#     return res


bunbo = 1
for i in range(1, n):
    # debug(i)
    bunbo = (bunbo * i) % p
debug("foo")
bunbo = inv(bunbo)
debug("hoge")

ans = 1
fact = prime_factorization(m)
for q in fact:
    debug(q)
    k = fact[q]
    cur = 1
    for i in range(k+1, n+k):
        cur = (cur * i) % p
    ans = (ans * cur) % p
ans = (ans * power(bunbo, len(fact))) % p
print(ans)
