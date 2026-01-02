import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,queue

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  n=I()
  s=S()

  a=[0]*n
  for i in range(n):
    if s[i]=='W':
      a[i]+=1
    if i<n-1:
      a[i+1]=a[i]

  b=[0]*n
  for i in range(n-1,-1,-1):
    if s[i]=='E':
      b[i]+=1
    if i-1>=0:
      b[i-1]=b[i]

  # print(a)
  # print(b)

  mn=inf
  for i in range(n):
    mn=min(mn,a[i]+b[i]-1)

  return mn

print(main())
