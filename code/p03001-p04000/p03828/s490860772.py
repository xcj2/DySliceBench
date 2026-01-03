import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

# Factoring by trial split
def getPrimeList(n):
  l=[]
  t=int(math.sqrt(n))+1
  
  for a in range(2,t):
    while n%a==0:
      n//=a
      l.append(a)
  
  if n!=1:
    l.append(n)
  
  return l

def main():
  l=[0]*1001

  n=I()

  for i in range(2,n+1):
    x=getPrimeList(i)
    for j in x:
      l[j]+=1

  sm=1
  for i in l:
    sm*=i+1

  return sm%mod

print(main())
