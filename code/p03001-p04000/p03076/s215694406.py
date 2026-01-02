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
  l=[I() for _ in range(5)]

  mn=inf
  for c in itertools.permutations(l,5):
    t=0
    for x in c:
      if t%10==0:
        t+=x
      else:
        t+=10-(t%10)
        t+=x

    mn=min(mn,t)

  return mn

# main()
print(main())
