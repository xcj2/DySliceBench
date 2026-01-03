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

  l.sort()

  if n%2==0:
    for i in range(n):
      if (i//2)*2+1!=l[i]:
        return 0
    return pow(2,n//2)%mod

  else:
    if l[0]!=0:
      return 0
    l=l[1:]
    for i in range(n-1):
      if (i//2)*2+2!=l[i]:
        return 0
    return pow(2,n//2)%mod

print(main())
