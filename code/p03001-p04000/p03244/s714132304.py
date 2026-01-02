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

  for i in range(len(l)):
    if i%2==0:
      l1.append(l[i])
    else:
      l2.append(l[i])

  l1.sort()
  l2.sort()

  a=[]
  b=[]

  p=l1[0]
  c=1
  mx=1
  for x in l1[1:]:
    if x==p:
      c+=1
    else:
      a.append([p,c])
      c=1
      p=x
  a.append([p,c])

  p=l2[0]
  c=1
  mx=1
  for x in l2[1:]:
    if x==p:
      c+=1
    else:
      b.append([p,c])
      c=1
      p=x
  b.append([p,c])

  a=sorted(a,key=lambda x:x[1],reverse=True)
  b=sorted(b,key=lambda x:x[1],reverse=True)

  if a[0][0]==b[0][0]:
    if len(a)==1 and len(b)==1:
      return n//2
    # if a[0][1]<b[0][1]:
    #   return n-a[1][1]-b[0][1]
    # return n-a[0][1]-b[1][1]
    else:
      return min(n-a[0][1]-b[1][1],n-a[1][1]-b[0][1])
  return n-a[0][1]-b[0][1]

print(main())
