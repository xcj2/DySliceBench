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
  la=['M','A','R','C','H']
  lb=[0]*5

  for _ in range(n):
    s=S()
    if la.count(s[0])>0:
      lb[la.index(s[0])]+=1

  sm=0

  for x in list(itertools.combinations(la,3)):
    sm+=lb[la.index(x[0])]*lb[la.index(x[1])]*lb[la.index(x[2])]

  return sm

print(main())
