import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  l=list(S())

  for i in range(2):
    for j in range(2):
      for k in range(2):
        a=b=c=''
        if i==0:
          a='+'
        else:
          a='-'
        if j==0:
          b='+'
        else:
          b='-'
        if k==0:
          c='+'
        else:
          c='-'
        x=l[0]+a+l[1]+b+l[2]+c+l[3]
        ans=eval(x)

        if ans==7:
          return x+'=7'

print(main())
