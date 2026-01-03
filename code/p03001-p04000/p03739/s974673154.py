import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  n=I()
  l=LI()

  sm=0
  add1=0
  f=1
  for i in range(n):
    sm+=l[i]
    if f==1:
      if sm<=0:
        add1+=abs(sm)+1
        sm=1
      f=-1
    else:
      if sm>=0:
        add1+=abs(sm)+1
        sm=-1
      f=1

  sm=0
  add2=0
  f=-1
  for i in range(n):
    sm+=l[i]
    if f==1:
      if sm<=0:
        add2+=abs(sm)+1
        sm=1
      f=-1
    else:
      if sm>=0:
        add2+=abs(sm)+1
        sm=-1
      f=1

  return min(add1,add2)

print(main())
