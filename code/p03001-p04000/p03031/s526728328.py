import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  n,m=LI()
  l2=[]
  for _ in range(m):
    l2.append(LI())

  l3=LI()

  l=[]
  a=len(bin(1<<n))-3
  for i in range(1<<n):
    l.append(str(bin(i))[2:].zfill(a))

  cnt=0
  for x in l:
    x=list(x)

    f=True
    for i in range(len(l2)):

      y=l2[i]
      c=0

      for a in y[1:]:
        c+=int(x[a-1])

      # print(c,l3[i])
      if c%2==l3[i]:
        pass
      else:
        f=False
        break

    if f:
      cnt+=1

  return cnt

print(main())
