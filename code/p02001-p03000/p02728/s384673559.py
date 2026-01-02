import sys
input = sys.stdin.readline
sys.setrecursionlimit(2*10**5+100)

MAX = 2*10**5+100
MOD = 10**9+7
fact = [0]*MAX #fact[i]: i!
inv = [0]*MAX #inv[i]: iの逆元
finv = [0]*MAX #finv[i]: i!の逆元
fact[0] = 1
fact[1] = 1
finv[0] = 1
finv[1] = 1
inv[1] = 1
    
for i in range(2, MAX):
    fact[i] = fact[i-1]*i%MOD
    inv[i] = MOD-inv[MOD%i]*(MOD//i)%MOD
    finv[i] = finv[i-1]*inv[i]%MOD

def C(n, r):
    if n<r:
        return 0
    if n<0 or r<0:
        return 0
    return fact[n]*(finv[r]*finv[n-r]%MOD)%MOD

def dfs1(v, pv):
    res = 1
    M = 0
    
    for nv in G[v]:
        if nv==pv:
            continue
        
        num, res2 = dfs1(nv, v)
        res *= finv[num]*res2
        res %= MOD
        M += num
    
    res *= fact[M]
    res %= MOD
    st[v] = res
    chi[v] = M+1
    
    return M+1, res
    
def dfs2(v, pv):
    res = rt[pv]*fact[chi[v]]*fact[N-chi[v]-1]*pow(st[v], MOD-2, MOD)
    res *= finv[N-chi[v]]
    res %= MOD
    
    for nv in G[v]:
        if nv==pv:
            continue
        
        res *= finv[chi[nv]]*st[nv]
        res %= MOD
    
    rt[v] = res
    
    for nv in G[v]:
        if nv==pv:
            continue
        
        dfs2(nv, v)
    
N = int(input())
G = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

st = [-1]*N
rt = [-1]*N
chi = [-1]*N
dfs1(0, -1)
rt[0] = st[0]

for nv in G[0]:
    dfs2(nv, 0)

for rt_i in rt:
    print(rt_i)
