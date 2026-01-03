import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

# 10 -> n
def ten2n(a,n):
  x=a//n
  y=a%n
  if x:
    return ten2n(x,n)+str(y)
  return str(y)

def main():
  n=S()

  l=list(n)

  l2=[]
  for i in range(pow(2,len(n)-1)):
    l2.append(list(ten2n(i,2).zfill(len(n)-1)))

  sm=0
  for x in l2:
    s=''
    for i in range(len(x)):
      if x[i]=='0':
        s+=l[i]
      else:
        s+=l[i]+'+'
    if len(l)>1:
      s+=l[-1]
    sm+=eval(s)

  return sm


print(main())
