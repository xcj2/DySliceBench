import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  s=list(S())

  c1=c2=0
  f=True
  for x in s:
    if f:
      if x=='0':
        c1+=1
      f=False
    else:
      if x=='1':
        c1+=1
      f=True

  f=False
  for x in s:
    if f:
      if x=='0':
        c2+=1
      f=False
    else:
      if x=='1':
        c2+=1
      f=True

  # print(c1,c2)
  return min(c1,c2)

print(main())
