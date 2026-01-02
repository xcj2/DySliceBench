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
  l=[]

  for i in range(n):
    l.append(LI())

  if n==1:
    return 1

  l2=[]
  for i in range(n):
    l3=[]
    for j in range(n):
      if i!=j:
        l3.append([l[j][0]-l[i][0],l[j][1]-l[i][1]])
    l2.append(l3)

  mx=0
  for i in range(n):
    _x=l2[i]

    for x in _x:
      sm=0
      for j in range(n):
        if i!=j:
          _y=l2[j]
          for y in _y:
            if x==y:
              sm+=1
      mx=max(mx,sm)

  return n-mx-1

print(main())
