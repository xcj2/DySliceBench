
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
mod = 10**9+7
 
fact = [1,1]
finv = [1,1]
inv = [0,1]
 
for i in range(2,2*10**5+5):
    fact.append((fact[-1]*i)%mod)
    inv.append((inv[mod%i]*(mod-mod//i))%mod)
    finv.append((finv[-1]*inv[-1])%mod)
 
def nCr(n,r,mod):
      
    return (fact[n]*finv[r])%mod*finv[n-r]%mod

n = int(input())
e = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    e[a-1].append(b-1)
    e[b-1].append(a-1)

numl = [0]*n
resl = [0]*n
def dfs(x,pre):
    num = 0
    res = 1
    for nex in e[x]:
        if nex == pre:
            continue
        dfs(nex,x)
        num += numl[nex]
        res *= nCr(num,numl[nex],mod)*resl[nex]
        res %= mod
    numl[x] = num+1
    resl[x] = res

    return 

dfs(0,-1)

ans = [0]*n
ans[0] = resl[0]
def dfs2(x,pre):
    
    for nex in e[x]:
        if nex == pre:
            continue
        pres = [resl[x], numl[x], resl[nex], numl[nex]]
        resl[x] *= pow(nCr(numl[x]-1,numl[nex],mod)*resl[nex],mod-2,mod)
        resl[x] %= mod
        numl[x] -= numl[nex]
        resl[nex] *=  nCr(numl[x]+numl[nex]-1,numl[x],mod)*resl[x]
        resl[nex] %= mod
        numl[nex] += numl[x]
        ans[nex] = resl[nex]
        dfs2(nex,x)
        resl[x], numl[x], resl[nex], numl[nex] = pres
    return
dfs2(0,-1)
for i in ans:
    print(i)