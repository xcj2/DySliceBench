#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

# arc058_b

# input
H, W, A, B = map(int, input().split())
mod = 1000000007
# fermat
N = 0
fac = [1]
inv = [1]

def mypow(a, b):
    return _mypow(a, a, b)

def _mypow(p, a, b):
    if b == 1:
        return p
    n = (p*p) % mod
    c, r = divmod(b, 2)
    if r == 0:
        return _mypow(n, a, c)
    else:
        ret = _mypow(n, a, c) * p
        return ret % mod

def init_cmb(_N):
    global N, fac, inv
    N=_N
    fac = [1]
    for i in range(1, N+1):
        n = (fac[i-1] * i) % mod
        fac.append(n)
    inv = (N+1) * [1]
    inv[N] = mypow(fac[N], mod-2)
    for i in range(1, N)[::-1]:
        inv[i] = (inv[i+1] * (i+1)) % mod

def cmb(n, r):
    if (r<0 or n<r): raise Exception(n, r)
    if n>N: raise Exception(n)
    ret = fac[n] * inv[r] * inv[n-r]
    return ret % mod
init_cmb(100000*2)
# getans
def calc(h, w):
    h += -1
    w += -1
    return cmb(h+w, h)
ans = 0
for y in range(1, H-A+1):
    left = calc(y, B)
    right = calc((H-y+1), (W-B))
    ans += left*right
    ans %= mod
# output
print(ans)
