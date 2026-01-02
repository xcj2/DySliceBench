import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  l=[inf]*100001
  l[0]=0

  l2=[1]
  for i in range(1,10):
    a=pow(6,i)
    b=pow(9,i)
    if a<=100000:
      l2.append(a)
    if b<=100000:
      l2.append(b)
  l2.sort()

  n=I()

  for i in range(1,n+1):
    for x in l2:
      if i-x>=0:
        l[i]=min(l[i],l[i-x]+1)

  return l[n]

print(main())
