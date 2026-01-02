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

  zcnt=l.count(0)
  c=0
  i=0

  while True:
    if zcnt==n:
      break
    if i>=n:
      i=0
    if l[i]>0:
      c+=1
      while True:
        if i<n and l[i]>=1:
          l[i]-=1

          if l[i]==0:
            zcnt+=1

          i+=1
        else:
          break
    else:
      i+=1

  return c

print(main())
