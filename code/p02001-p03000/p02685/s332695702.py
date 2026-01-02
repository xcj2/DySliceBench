import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

com_mx=200005
mod=998244353
fac=[0]*com_mx
finv=[0]*com_mx
inv=[0]*com_mx
fac[0]=1
fac[1]=1
finv[0]=1
finv[1]=1
inv[1]=1
for i in range(2,com_mx):
  fac[i]=fac[i-1]*i%mod
  inv[i]=-inv[mod%i]*(mod//i)%mod
  finv[i]=finv[i-1]*inv[i]%mod

def com(n,k):
  if n<k or n<0 or k<0:
    return 0
  return fac[n]*(finv[k]*finv[n-k]%mod)%mod

def main():
  n,m,k=LI()
  res=0
  tmp=m*pow(m-1,n-k-1,mod)
   
  for r in range(n-k-1,n):
    res=(res+tmp*com(n-1,r)%mod)%mod
    tmp=tmp*(m-1)%mod
  return res

# main()
print(main())
