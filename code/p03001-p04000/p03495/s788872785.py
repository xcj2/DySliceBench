import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  n,k=LI()
  a=LI()

  a.sort()
  b=[]

  _a=a[0]
  c=1
  for x in a[1:]:
    if _a==x:
      c+=1
    else:
      b.append([_a,c])
      _a=x
      c=1
  b.append([_a,c])

  b=sorted(b,key=lambda x:x[1])

  ans=0
  for i in range(len(b)-k):
    ans+=b[i][1]

  return ans

print(main())
