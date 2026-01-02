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

class ComMod():
  def __init__(self,n_max,mod):
    self.mod=mod
    self.fact=[0]*(n_max+1)
    self.ifact=[0]*(n_max+1)
    self.fact[0]=1  
    for i in range(1,n_max+1):
      self.fact[i]=self.fact[i-1]*i
      self.fact[i]%=mod
    self.ifact[n_max]=pow(self.fact[n_max],mod-2,mod)
    for i in range(n_max,0,-1):
      self.ifact[i-1]=self.ifact[i]*i
      self.ifact[i-1]%=mod
  def com(self,n,k):
    if n<0 or k<0 or n<k:
      return 0
    return self.fact[n]*(self.ifact[k]*self.ifact[n-k]%self.mod)%self.mod

def main():
  n,m,k=LI()
  res=0
  mod=998244353
  tmp=m*pow(m-1,n-k-1,mod)

  c=ComMod(200005,mod)

  for r in range(n-k-1,n):
    res=(res+tmp*c.com(n-1,r)%mod)%mod
    tmp=tmp*(m-1)%mod
  return res

# main()
print(main())
