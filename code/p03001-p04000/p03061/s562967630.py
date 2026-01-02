import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,queue

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

# GCD
def gcd(x,y):
  while y:
    x,y=y,x%y
  return x

def main():
  n=I()
  l=LI()

  l1=[l[0]]
  for i in range(1,n):
    l1.append(gcd(l1[i-1],l[i]))

  l2=[l[-1]]
  for i in range(1,n):
    l2.append(gcd(l2[i-1],l[n-i-1]))
  l2.reverse()

  mx=max(l1[-2],l2[1])
  for i in range(n-2):
    mx=max(mx,gcd(l1[i],l2[i+2]))

  return mx

print(main())
