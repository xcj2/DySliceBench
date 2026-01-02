import sys
def input():return sys.stdin.readline()[:-1]
def N(): return int(input())
def NM():return map(int,input().split())
def L():return list(NM())
def LN(n):return [N() for i in range(n)]
def LL(n):return [L() for i in range(n)]
k=N()
s=input()
n=len(s)
N=k+n
mod=10**9+7
fac=[1]*(N+3)
inv=[1]*(N+3)
t=1
for i in range(1,N+3):
    t*=i
    t%=mod
    fac[i]=t
t=pow(fac[N+2],mod-2,mod)
for i in range(N+2,0,-1):
    inv[i]=t
    t*=i
    t%=mod
def comb(n,r):
    if r>n or r<0:
        return 0
    return fac[n]*inv[n-r]*inv[r]%mod
pow26=[1]*(k+1)
pow25=[1]*(k+1)
t1=1
t2=1
for i in range(k+1):
    pow25[i]=t1
    pow26[i]=t2
    t1*=25
    t1%=mod
    t2*=26
    t2%=mod
ans=pow26[k]
for i in range(1,k+1):
    ans+=comb(n+i-1,i)*pow25[i]*pow26[k-i]
    ans%=mod
print(ans)
