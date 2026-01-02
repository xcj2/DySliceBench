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
  b=LI()

  l1=[a[0]]
  for i in range(1,len(a)):
    l1.append(l1[i-1]+a[i])

  b.reverse()
  l2=[b[0]]
  for i in range(1,len(b)):
    l2.append(l2[i-1]+b[i])
  l2.reverse()

  # print(l1)
  # print(l2)

  mx=0
  for i in range(n):
    mx=max(mx,l1[i]+l2[i])

  return mx

print(main())
