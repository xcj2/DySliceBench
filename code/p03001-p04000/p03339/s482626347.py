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
  l=list(S())

  l1=[0]*n
  for i in range(n):
    if l[i]=='E':
      l1[i]+=1

  for i in range(1,n):
    l1[i]+=l1[i-1]

  l2=[]
  for i in range(n):
    l2.append(i+1-l1[i])

  mn=inf
  for i in range(n):
    if l[i]=='W':
      a=l2[i]-1
    else:
      a=l2[i]
    mn=min(mn,l1[-1]-l1[i]+a)

  return mn

print(main())
