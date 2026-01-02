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
  n,p=LI()

  if n==1:
    print(p)
    exit()
  
  l=getPrimeList(p)
  
  if len(l)==0:
    print(1)
    exit()

  a=l[0]
  c=1
  sm=1
  for x in l[1:]:
    if a==x:
      c+=1
    else:
      c=1
      a=x

    if c==n:
      sm*=a
      c=0

  return sm

print(main())
