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

  if n==1:
    return l[0]

  cen=l[0]
  l.remove(cen)

  la=[]
  lb=[]
  for i in range(len(l)):
    if i%2==0:
      la.append(l[i])
    else:
      lb.append(l[i])

  if n%2==0:
    la.reverse()
    return ' '.join(str(x) for x in la)+' '+str(cen)+' '+' '.join(str(x) for x in lb)
  else:
    lb.reverse()
    return ' '.join(str(x) for x in lb)+' '+str(cen)+' '+' '.join(str(x) for x in la)

print(main())
