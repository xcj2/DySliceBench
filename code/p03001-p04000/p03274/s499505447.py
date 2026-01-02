import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  n,k=LI()
  l=LI()

  if l.count(0)>0:
    k-=1
    l.remove(0)

  if k==0:
    print(0)
    exit()

  if len(l)==0:
    print(0)
    exit()

  idx=len(l)-1
  for i in range(len(l)):
    if l[i]>0:
      idx=i
      break
  if max(l)<0:
    idx=len(l)

  l1=[abs(x) for x in l[idx:]]
  l2=[abs(x) for x in l[:idx]]
  l2.reverse()

  # print(l1)
  # print(l2)

  mn=inf
  for i in range(len(l1)):
    if i+1>=k:
      mn=min(mn,l1[i])
    else:
      if len(l2)>=k-(i+1):
        # print(l1[i],l2[k-(i+1)-1])
        mn=min(mn,l1[i]+2*l2[k-(i+1)-1])

  for i in range(len(l2)):
    if i+1>=k:
      mn=min(mn,l2[i])
    else:
      if len(l1)>=k-(i+1):
        # print(l2[i],l1[k-(i+1)-1])
        mn=min(mn,l2[i]+2*l1[k-(i+1)-1])

  print(mn)

main()
# print(main())
