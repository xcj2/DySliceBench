import sys
sys.setrecursionlimit(1<<30)
mod = 10**9+7
def inv(x):
    return pow(x,mod-2,mod)
def dfs_size(x):
    sizex = 1
    for y in edges[x]:
        if y != parent[x]:
            parent[y] = x
            sizex += dfs_size(y)
    size[x] = sizex
    return sizex
def dfs_dp(x):
    dpx = 1
    for y in edges[x]:
        if y != parent[x]:
            dpx *= dfs_dp(y)
            dpx *= inv_fac[size[y]]
            dpx %= mod
    dpx *= fac[size[x]-1]
    dpx %= mod
    dp[x] = dpx
    return dpx

def dfs_ans(x):
    ansx = 1
    if x != 1:
        for y in edges[x]:
            if y != parent[x]:
                ansx *= dp[y]
                ansx *= inv_fac[size[y]]
                ansx %= mod
            else:
                dpy = ans[y]
                dpy *= inv_fac[N-1]
                dpy *= fac[size[x]]
                dpy *= fac[N-size[x]-1]
                dpy *= inv(dp[x])
                dpy %= mod
                ansx *= dpy
                ansx *= inv_fac[N-size[x]]
                ansx %= mod
        ansx *= fac[N-1]
        ansx %= mod
        ans[x] = ansx
    for y in edges[x]:
        if y != parent[x]:
            dfs_ans(y)
N = int(input())
edges = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)
size = [0]*(N+1)
parent = [0]*(N+1)
dfs_size(1)
fac = [1]
for i in range(1,N+1):
    fac.append(fac[-1]*i % mod)
inv_fac = [inv(fac[N])]
for i in range(1,N+1)[::-1]:
    inv_fac.append(inv_fac[-1]*i % mod)
inv_fac = inv_fac[::-1]
dp = [0]*(N+1)
dfs_dp(1)
ans = [0]*(N+1)
ans[1] = dp[1]
dfs_ans(1)
for i in ans[1:]:
    print(i)