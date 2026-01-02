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
  n=I()
  a=[LI() for _ in range(n)]
  b=[LI() for _ in range(n)]

  ans=-inf
  for i in range(1,1<<10):
    _ans=0
    for _i,x in enumerate(a):
      counter=0
      for j in range(10):
        if i&(1<<j) and x[j]==1:
          counter+=1
      _ans+=b[_i][counter]
    ans=max(ans,_ans)
  return ans

# main()
print(main())
