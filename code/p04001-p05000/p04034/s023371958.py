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
  l=[0]*n
  l2=[1]*n

  l[0]=1

  for _ in range(m):
    x,y=LI()
    l2[y-1]+=1
    l2[x-1]-=1

    if l[x-1]>0:
      l[y-1]+=1

      if l2[x-1]==0:
        l[x-1]=0

  sm=0
  for x in l:
    if x>0:
      sm+=1
  return sm

# main()
print(main())
