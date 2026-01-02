import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

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

  l1=l[:]
  l2=l[:]

  for i in range(1,n):
    l1[i]=gcd(l1[i-1],l1[i])

  for i in range(n-1,0,-1):
    l2[i-1]=gcd(l2[i],l2[i-1])

  n+=1
  l1=[0]+l1
  l2=l2+[0]

  # print(l1)
  # print(l2)

  mx=0
  for i in range(n-1):
    mx=max(mx,gcd(l1[i],l2[i+1]))

  return mx

print(main())
