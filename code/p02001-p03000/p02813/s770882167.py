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
  p=LI()
  q=LI()

  a=[i+1 for i in range(n)]
  ansa=0
  ansb=0
  for j,x in enumerate(itertools.permutations(a)):
    f1=True
    f2=True
    for i in range(n):
      if x[i]!=p[i]:
        f1=False
      if x[i]!=q[i]:
        f2=False
    if f1:
      ansa=j+1
    if f2:
      ansb=j+1

  # print(ansa,ansb)
  return abs(ansa-ansb)

# main()
print(main())
