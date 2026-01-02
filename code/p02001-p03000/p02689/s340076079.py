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

def main():
  n,m=LI()
  l=LI()

  ll=[[] for _ in range(n)]

  for _ in range(m):
    a,b=LI()
    a-=1
    b-=1
    ll[a].append(b)
    ll[b].append(a)

  ans=0
  for i,h in enumerate(l):
    mx=-inf
    f=True
    for x in ll[i]:
      mx=max(mx,l[x])
      if h<=mx:
        f=False
        break
    if f:
      ans+=1

  return ans

# main()
print(main())
