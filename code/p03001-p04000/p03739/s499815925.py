import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  n=II()
  l=LI()

  ad1=0
  f=True
  sm=0
  for x in l:
    if f:
      sm+=x
      if sm<=0:
        ad1+=abs(sm)+1
        sm=1
      f=False
    else:
      sm+=x
      if sm>=0:
        ad1+=abs(sm)+1
        sm=-1
      f=True

  ad2=0
  f=False
  sm=0
  for x in l:
    if not f:
      sm+=x
      if sm>=0:
        ad2+=abs(sm)+1
        sm=-1
      f=True
    else:
      sm+=x
      if sm<=0:
        ad2+=abs(sm)+1
        sm=1
      f=False

  return min(ad1,ad2)

print(main())
