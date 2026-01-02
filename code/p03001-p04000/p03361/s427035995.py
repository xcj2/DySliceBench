import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  h,w=LI()

  l=[]
  for i in range(h):
    l.append(S())

  a=[[0,-1],[-1,0],[1,0],[0,1]]

  for i in range(h):
    for j in range(w):
      b=l[i][j]
      f=True
      if b=='#':
        for k in a:
          _i=i
          _j=j
          _i+=k[0]
          _j+=k[1]
          if _i>=0 and _i<=h-1 and _j>=0 and _j<=w-1:
            if l[_i][_j]=='#':
              f=False
        if f:
          return 'No'
          exit()
  return 'Yes'


print(main())
