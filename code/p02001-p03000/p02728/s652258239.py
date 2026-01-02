import os, sys, bisect, copy
from collections import defaultdict, Counter, deque
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
def input(): return sys.stdin.readline()
def mapi(arg=0): return map(int if arg==0 else str,input().split())
#------------------------------------------------------------------
sys.setrecursionlimit(100005)
mod = 1000000007
N=int(2*1e5+100)
sz = [0]*N
dp = [0]*N
gr = defaultdict(list)
def modPow(a,b):
    ans=1
    while (b):
        if (b&1): ans=(ans*a)%mod
        b>>=1
        a=(a*a)%mod
    return ans

def modInv(x):
    return modPow(x,mod-2)

def dfs(x, par):
    sz[x]=1
    for item in gr[x]:
        if item==par: continue
        dfs(item,x)
        sz[x]+=sz[item]

def dfs1(x, par):
    for item in gr[x]:
        if item==par: continue
        dp[item]=(dp[x]*(n-sz[item]))%mod
        dp[item]=(dp[item]*modInv(sz[item]))%mod
        dfs1(item,x)

n = int(input())
for i in range(n-1):
    x,y = mapi()
    gr[x].append(y)
    gr[y].append(x)
dfs(1,0)
dp[1]=1
for i in range(1,n+1):
    dp[1]=(dp[1]*sz[i])%mod
dfs1(1,0)
res = 1
for i in range(1,n+1):
    res = (res*i)%mod
for i in range(1,n+1):
    dp[i]=(res*modInv(dp[i]))%mod
for i in range(1,n+1):
    print(dp[i])
