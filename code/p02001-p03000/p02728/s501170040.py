import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

# nCk
## 0!~n!をmodしつつ求める
def fact_all(n,M=mod):
    f = [1]*(n+1)
    ans = 1
    for i in range(1,n+1):
        ans = (ans*i)%M
        f[i] = ans
    return f

## inv(0!)~inv(n!)をmodしつつ求める
def fact_inv_all(fact_all,M=mod):
    N = len(fact_all)
    finv = [0]*N
    finv[-1] = pow(fact_all[-1],M-2,M)
    for i in range(N-1)[::-1]:
        finv[i] = finv[i+1]*(i+1)%M
    return finv

## nCkをmodしつつ返す
def nCk(n,k,fact_list,inv_list,M=mod):
    return (((fact_list[n]*inv_list[k])%M)*inv_list[n-k])%M

def edges_to_pt(s,t,n,directed=False):
    pt = [[] for _ in range(n)]
    for i in range(len(s)):
        pt[s[i]-1].append(t[i]-1)
        if not directed:
            pt[t[i]-1].append(s[i]-1)
    return pt

def order_dfs(pt,N):
    s = 0
    parent = [-1]*N
    order = [s]
    visited = [False]*N
    visited[s] = True
    S = [s]
    while S:
        v = S.pop()
        for u in pt[v]:
            if not visited[u]:
                visited[u] = True
                order.append(u)
                parent[u] = v
                S.append(u)
    return order,parent

N = I()
a,b = LIR(N-1,2)
pt = edges_to_pt(a,b,N)

fl = fact_all(N)
il = fact_inv_all(fl)

order,parent = order_dfs(pt,N)
order = order[::-1]

# 順方向の部分木について数え上げ（葉側から順に行う）
visited = [False]*N
size = [0]*N
dp = [1]*N
for v in order:
    # 葉の処理
    if len(pt[v]) == 1 and not visited[pt[v][0]]:
        dp[v] = 1
        size[v] = 1
    # 葉以外での処理
    else:
        size_v = 0
        for u in pt[v]:
            size_v += size[u]
            dp[v] *= dp[u]*il[size[u]]
            dp[v] %= mod
        dp[v] *= fl[size_v]
        dp[v] %= mod
        size[v] = size_v + 1
    visited[v] = True

# 逆側の部分木について数え上げ（根側から順に行う）
dp2 = [1]*N
for v in order[::-1]:
    p = parent[v]
    # 根の処理
    if p == -1:
        dp2[v] = 1
    # 根以外での処理
    else:
        dp2[v] = (((dp[p]*dp2[p]*pow(dp[v],mod-2,mod))%mod
                    *fl[N-1-size[v]]*il[size[p]-1])%mod
                    *fl[size[v]]*il[N-size[p]])%mod

# 部分木の情報を統合
for v in range(N):
    ans = (fl[N-1]*il[size[v]-1]*il[N-size[v]]*dp[v]*dp2[v])%mod
    print(ans)