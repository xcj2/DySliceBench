import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  n,m=LI()
  l=[]
  for _ in range(m):
    a=LI()
    l.append(a[1:])

  lp=LI()

  a=[]
  for i in range(1<<n):
    _a=[]
    for j in range(n):
      if i&(1<<j):
        _a.append(1)
      else:
        _a.append(0)
    a.append(_a)

  ans=0
  for x in a:
    f=True
    for i,y in enumerate(l):
      _sum=0
      for z in y:
        _sum+=x[z-1]
      if _sum%2!=lp[i]:
        f=False
        break
    if f:
      ans+=1

  return ans

# main()
print(main())
