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

  l=[LI() for _ in range(n-1)]

  for i in range(n-1):
    t=0
    for x in l[i:]:
      c,s,f=x
      if t<=s:
        t=s
      else:
        _t=t-s
        if _t%f==0:
          pass
        else:
          t+=f-(_t%f)
      t+=c
    print(t)
  print(0)

main()
# print(main())
