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

# nCr(mod) -- START --
class ComMod():
  def __init__(self,n,mod):
    self.n=n
    self.mod=mod
    self.fact=[0]*(n+1)
    self.ifact=[0]*(n+1)
    self.fact[0]=1  
    for i in range(1,n+1):
      self.fact[i]=self.fact[i-1]*i
      self.fact[i]%=self.mod
    self.ifact[n]=pow(self.fact[n],self.mod-2,self.mod)
    for i in range(n,0,-1):
      self.ifact[i-1]=self.ifact[i]*i
      self.ifact[i-1]%=self.mod
  def com(self,n,k):
    if n<0 or k<0 or n<k:
      return 0
    return self.fact[n]*(self.ifact[k]*self.ifact[n-k]%self.mod)%self.mod
# nCr(mod) --- END ---

# n^p(mod m) -- START --
def powMod(n,p,m):
  if p==0:
    return 1
  if p%2==0:
    t=powMod(n,p//2,m)
    return t*t%m
  return n*powMod(n,p-1,m)%m
# n^p(mod m) --- END ---

def main():
  n,m,k=LI()
  mod=998244353
  c=ComMod(200005,mod)

  ans=0
  for i in range(k+1):
    # print(m,c.com(n-1,i),powMod(m-1,n-1-k,mod))
    ans=(ans+m*c.com(n-1,i)*powMod(m-1,n-1-i,mod))%mod

  return ans

# main()
print(main())
