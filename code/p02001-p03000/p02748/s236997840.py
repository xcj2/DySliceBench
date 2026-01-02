import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=998244353
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  a,b,m=LI()
  la=LI()
  lb=LI()
  l=[LI() for _ in range(m)]

  ans=min(la)+min(lb)
  for x,y,c in l:
    x-=1
    y-=1
    _ans=la[x]+lb[y]-c
    ans=min(ans,_ans)

  return ans

# main()
print(main())
