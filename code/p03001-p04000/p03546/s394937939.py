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
  d=[]
  for _ in range(10):
    d.append(LI())

  for k in range(10):
    for i in range(10):
      for j in range(10):
        d[i][j]=min(d[i][j],d[i][k]+d[k][j])

  ans=0
  for _ in range(n):
    l=LI()
    for x in l:
      if x not in (1,-1):
        ans+=d[x][1]

  return ans

# main()
print(main())
