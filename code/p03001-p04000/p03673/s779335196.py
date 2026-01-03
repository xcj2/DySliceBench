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
  l=LS()

  l1=[]
  l2=[]

  for i in range(len(l)):
    if i%2==0:
      l1.append(l[i])
    else:
      l2.append(l[i])

  if n%2==0:
    l2.reverse()
    l2+=l1
    return ' '.join(str(x) for x in l2)
  else:
    l1.reverse()
    l1+=l2
    return ' '.join(str(x) for x in l1)

print(main())
