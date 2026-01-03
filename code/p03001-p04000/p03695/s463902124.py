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
  l=LI()

  a=[1,400,800,1200,1600,2000,2400,2800,3200]
  b=[0]*9
  c=0
  for x in l:
    for i in range(len(a)-1):
      if a[i]<=x and x<a[i+1]:
        b[i]+=1

    if 3200<=x:
      c+=1

  d=0
  for x in b:
    if x>0:
      d+=1

  if d==0:
    print(1,c)
  else:
    print(d,d+c)

main()
