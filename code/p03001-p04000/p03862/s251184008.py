import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  n,m=LI()

  l=LI()

  cnt=0

  for i in range(n-2):
    if l[i]+l[i+1]<=m:
      continue
    else:
      if l[i]>m:
        a=l[i+1]
        b=max(0,l[i]+l[i+1]-m)
        cnt+=b
        l[i+1]=0
      else:
        b=max(0,l[i]+l[i+1]-m)
        cnt+=b
        l[i+1]-=b

  cnt+=max(0,l[-1]+l[-2]-m)

  return cnt

print(main())
