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

  l1=[]
  l2=[]

  f=True
  for x in l:
    if f:
      f=False
      l1.append(x)
    else:
      f=True
      l2.append(x)

  l1.sort()
  l2.sort()

  l3=[]
  l4=[]

  a=l1[0]
  c=1
  for x in l1[1:]:
    if a==x:
      c+=1
    else:
      l3.append([a,c])
      a=x
      c=1
  l3.append([a,c])

  a=l2[0]
  c=1
  for x in l2[1:]:
    if a==x:
      c+=1
    else:
      l4.append([a,c])
      a=x
      c=1
  l4.append([a,c])

  l3=sorted(l3,key=lambda x:x[1],reverse=True)
  l4=sorted(l4,key=lambda x:x[1],reverse=True)

  if l3[0][0]==l4[0][0]:
    if len(l3)==1 and len(l4)==1:
      return n//2
    elif len(l3)==1:
      return n-l3[0][1]-l4[1][1]
    elif len(l4)==1:
      return n-l3[1][1]-l4[0][1]
    else:
      return min(n-l3[0][1]-l4[1][1],n-l3[1][1]-l4[0][1])
  else:
    return n-l3[0][1]-l4[0][1]

print(main())
