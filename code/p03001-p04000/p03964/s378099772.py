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
  t,a=LI()
  l=[LI() for _ in range(n-1)]

  # t<=nt' and a<=na'
  # t/t'<=n and a/a'<=n
  for _t,_a in l:
    _n=max(-(-t//_t),-(-a//_a))
    t=_n*_t
    a=_n*_a

  return t+a

# main()
print(main())
