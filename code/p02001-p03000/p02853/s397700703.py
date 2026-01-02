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
  x,y=LI()
  ans=0

  if x==3:
    ans+=100000
  elif x==2:
    ans+=200000
  elif x==1:
    ans+=300000
  if y==3:
    ans+=100000
  elif y==2:
    ans+=200000
  elif y==1:
    ans+=300000
  if x==1 and y==1:
    ans+=400000
  return ans

# main()
print(main())
