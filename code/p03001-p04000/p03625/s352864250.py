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

  a=[]
  b=[]
  for x in l:
    if len(a)>0:
      if x==a[-1]:
        a.pop()
        b.append(x)
      else:
        a.pop()
        a.append(x)
    else:
      a.append(x)

  b.sort()

  if len(b)<2:
    return 0

  return b[-1]*b[-2]

print(main())
