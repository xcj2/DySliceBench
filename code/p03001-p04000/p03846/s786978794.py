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
    for i in range(n//2):
      if l[i]!=i//2*2+1:
        return 0
  else:
    if l[0]!=0:
      return 0
    for i in range(1,n):
      if -(-i//2)*2!=l[i]:
        return 0
  return pow(2,n//2)%mod

print(main())
