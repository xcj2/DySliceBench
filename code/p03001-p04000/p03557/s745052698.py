import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  N=II()
  l1=LI()
  l2=LI()
  l3=LI()

  l=[]
  for x in l1:
    l.append([x,3])

  for x in l2:
    l.append([x,2])

  for x in l3:
    l.append([x,1])

  l=sorted(l,key=lambda x:[x[0],x[1]])

  a=0
  b=c=N
  cnt=0
  for x in l:
    y=x[1]
    if y==3:
      a+=1
    elif y==1:
      c-=1
    else:
      cnt+=a*c
      b-=1

  return cnt

# main()
print(main())
