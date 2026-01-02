#!/usr/bin/env python3
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

MOD = 10**9 + 7
MAX_N = 10**6

fac = [1] + [0] * MAX_N
for i in range(1, MAX_N+1):
    fac[i] = fac[i-1] * (i) % MOD

fac_inv = [1] + [0] * MAX_N
fac_inv[MAX_N] = pow(fac[MAX_N], MOD-2, MOD)
for i in range(MAX_N, 1, -1):
    fac_inv[i-1] = fac_inv[i] * i % MOD

def mod_nCr(n, r):
    if n < r or n < 0 or r < 0:
        return 0
    tmp = fac_inv[n-r] * fac_inv[r] % MOD
    return tmp * fac[n] % MOD

n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = [int(item) - 1 for item in input().split()]
    edge[a].append(b)
    edge[b].append(a)

f_cnt = [0] * n
f_dp = [0] * n
def dfs1(p, v):
    val = 1
    cnt = 0
    for nv in edge[v]:
        if nv == p:
            continue
        ncnt, nval = dfs1(v, nv)
        val *= mod_nCr(cnt + ncnt, ncnt) 
        val *= nval
        val %= MOD
        cnt += ncnt
    f_cnt[v] = cnt + 1
    f_dp[v] = val
    return (cnt+1, val)

b_dp = [0] * n
def dfs2(p, v, pval):
    val = 1
    cnt = 0
    p_cnt = n - f_cnt[v]
    for nv in edge[v]:
        if nv == p:
            ncnt = p_cnt
            nval = pval
        else:
            ncnt, nval = f_cnt[nv], f_dp[nv]
        coef = mod_nCr(cnt + ncnt, ncnt) * nval % MOD
        val = val * coef % MOD
        b_dp[v] = val
        cnt += ncnt
    i = 0
    for nv in edge[v]:
        if nv == p:
            continue
        ncnt, nval = f_cnt[nv], f_dp[nv]
        coef = mod_nCr(n - 1, ncnt) * nval % MOD
        pp = val * pow(coef, MOD-2, MOD) % MOD
        i += 1
        dfs2(v, nv, pp)

dfs1(-1, 0)
dfs2(-1, 0, 1)
for item in b_dp:
    print(item)