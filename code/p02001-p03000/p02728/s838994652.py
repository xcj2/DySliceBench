import sys
sys.setrecursionlimit(10**7)
mod = 10**9+7
fact = [1]*(2*10**5+1)
for n in range(1,2*10**5+1):
    fact[n] = n*fact[n-1]%mod
factinv = [1]*(2*10**5+1)
inv = [1]*(2*10**5+1)
for n in range(1,2*10**5+1):
    factinv[n] = pow(fact[n],mod-2,mod)
    inv[n] = pow(n,mod-2,mod)
def comb(n,k):
    return fact[n]*factinv[k]*factinv[n-k]%mod

N = int(input())
g = [[] for _ in range(N)]

for i in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

p = [-1]*N
p[0] = 0
q = [0]
while q:
    i = q.pop()
    for j in g[i]:
        if p[j]==-1:
            p[j] = i
            q.append(j)

c = [[] for _ in range(N)]
for i in range(1,N):
    c[p[i]].append(i)

cn = [-1]*N
def rec(n):
    if cn[n] != -1:
        return cn[n]
    res = 0
    for i in c[n]:
        res += rec(i)+1
    cn[n] = res
    return res

cn[0] = rec(0)    

ans = [0]*N

def dfs(n):
    res = fact[cn[n]]
    for c in g[n]:
        if c==p[n]:
            continue
        res *= factinv[cn[c]+1]*dfs(c)
        res %= mod
    return res

ans[0] = dfs(0)

q = [0]
while q:
    i = q.pop()
    for j in g[i]:
        if ans[j]==0:
            ans[j] = ans[i]*(cn[j]+1)*inv[N-1-cn[j]]%mod
            q.append(j)

for i in range(N):
    print(ans[i])
