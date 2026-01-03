import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  _n,_m=LI()

  ans=1
  ans2=1
  if abs(_n-_m)>1:
    return 0
    exit()
  else:
    n=_n
    m=_m
    while True:
      if n==0 or m==0:
        break
      ans*=n
      n-=1
      ans%=mod
      ans*=m
      m-=1
      ans%=mod
    n=_n
    m=_m
    while True:
      if n==0 or m==0:
        break
      ans2*=n
      n-=1
      ans2%=mod
      ans2*=m
      m-=1
      ans2%=mod
    if abs(_n-_m)==1:
      return ans%mod
    return (ans+ans2)%mod

print(main())
