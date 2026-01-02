import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  N,M=LI()
  l1=[]
  l2=[]
  l3=[]
  l4=[]
  l5=[]
  l6=[]
  l7=[]
  l8=[]
  for _ in range(N):
    _l=LI()

    l1.append(sum([_l[0],_l[1],_l[2]]))
    l2.append(sum([_l[0],_l[1],-_l[2]]))
    l3.append(sum([_l[0],-_l[1],_l[2]]))
    l4.append(sum([_l[0],-_l[1],-_l[2]]))
    l5.append(sum([-_l[0],_l[1],_l[2]]))
    l6.append(sum([-_l[0],_l[1],-_l[2]]))
    l7.append(sum([-_l[0],-_l[1],_l[2]]))
    l8.append(sum([-_l[0],-_l[1],-_l[2]]))

  l1=sorted(l1,key=lambda x:x,reverse=True)
  l2=sorted(l2,key=lambda x:x,reverse=True)
  l3=sorted(l3,key=lambda x:x,reverse=True)
  l4=sorted(l4,key=lambda x:x,reverse=True)
  l5=sorted(l5,key=lambda x:x,reverse=True)
  l6=sorted(l6,key=lambda x:x,reverse=True)
  l7=sorted(l7,key=lambda x:x,reverse=True)
  l8=sorted(l8,key=lambda x:x,reverse=True)

  x1=sum(l1[:M])
  x2=sum(l2[:M])
  x3=sum(l3[:M])
  x4=sum(l4[:M])
  x5=sum(l5[:M])
  x6=sum(l6[:M])
  x7=sum(l7[:M])
  x8=sum(l8[:M])

  return max(x1,x2,x3,x4,x5,x6,x7,x8)

# main()
print(main())
