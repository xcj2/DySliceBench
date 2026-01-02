# ABC133-B

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
  n,d=LI()
  l=[LI() for _ in range(n)]

  c=0
  for i in range(n):
    for j in range(i+1,n):
      x=l[i]
      y=l[j]

      sm=0
      for k in range(d):
        sm+=(x[k]-y[k])*(x[k]-y[k])

      # print(sm)

      a=math.sqrt(sm)
      if a==int(a) and a*a==sm:
        c+=1

  return c

print(main())
