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

  l=[]
  for _ in ' '*m:
    a,b=LI()
    l.append([a,1])
    l.append([b,-1])

  l=sorted(l,key=lambda x:x[1],reverse=True)
  l=sorted(l,key=lambda x:x[0])

  sm=st=0
  for x in l:
    sm+=x[1]
    if sm==m:
      st=x[0]
    if sm!=m and st!=0:
      return x[0]-st+1

  return 0

print(main())
