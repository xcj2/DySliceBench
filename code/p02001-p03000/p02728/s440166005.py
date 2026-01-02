import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

MAX = 2*10**5+100
fact = [0]*MAX
inv = [0]*MAX
finv = [0]*MAX
MOD = 10**9+7
 
def C_init():
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
    nums = []
    res = 1
    
    for nv in G[v]:
        if nv==pv:
            continue
        
        num, chi_res = dfs1(nv, v)
        nums.append(num)
        res *= chi_res
        res %= MOD
    
    M = sum(nums)
    A1[v] = M+1
    
    for num in nums:
        res *= C(M, num)
        res %= MOD
        M -= num
    
    A2[v] = res
    
    return A1[v], A2[v]
    
def dfs2(v, pv):
    res = A3[pv]*pow(C(N-1, A1[v])*A2[v], MOD-2, MOD)%MOD
    M = N-1
    res *= C(M, N-A1[v])
    M -= N-A1[v]
    
    for nv in G[v]:
        if nv==pv:
            continue
        
        res *= A2[nv]
        res *= C(M, A1[nv])
        M -= A1[nv]
        res %= MOD
    
    A3[v] = res
    
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

C_init()
A1 = [-1]*N
A2 = [-1]*N
A3 = [-1]*N
dfs1(0, -1)
A3[0] = A2[0]

for nv in G[0]:
    dfs2(nv, 0)

for A3i in A3:
    print(A3i)