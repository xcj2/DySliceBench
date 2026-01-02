import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

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
  n,a,b=LI()

  ans=powMod(2,n,mod)
  ans-=1
  ans%=mod

  pattern_a1=1
  for i in range(a):
    pattern_a1*=n-i
    pattern_a1%=mod
  pattern_a2=1
  for i in range(1,a+1):
    pattern_a2*=i
    pattern_a2%=mod
  pattern_a=pattern_a1*pow(pattern_a2,mod-2,mod)

  pattern_b1=1
  for i in range(b):
    pattern_b1*=n-i
    pattern_b1%=mod
  pattern_b2=1
  for i in range(1,b+1):
    pattern_b2*=i
    pattern_b2%=mod
  pattern_b=pattern_b1*pow(pattern_b2,mod-2,mod)

  ans-=pattern_a
  ans%=mod
  if ans<0:
    ans+=mod
  ans-=pattern_b
  ans%=mod
  if ans<0:
    ans+=mod

  return ans

# main()
print(main())
