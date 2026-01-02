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
  a=LI()

  a.sort()

  b=a[0]
  c=1
  sm=0
  for x in a[1:]:
    if b==x:
      c+=1
    else:
      if c==b:
        pass
      elif c>b:
        sm+=c-b
      else:
        sm+=c

      c=1
      b=x

  if c==b:
    pass
  elif c>b:
    sm+=c-b
  else:
    sm+=c

  return sm

print(main())
