import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  n=II()
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

  a1=[l1[0],1]
  a2=[0,0]
  b1=[l2[0],1]
  b2=[0,0]

  _a=l1[0]
  c1=1
  for x in l1[1:]:
    if _a==x:
      c1+=1
    else:
      if c1>a1[1]:
        if a1[0]!=l1[0]:
          a2[0]=a1[0]
          a2[1]=a1[1]
        a1[0]=_a
        a1[1]=c1
      elif c1>a2[1]:
        if a1[0]!=_a:
          a2[0]=_a
          a2[1]=c1
      _a=x
      c1=1
  if c1>a1[1]:
    if a1[0]!=l1[0]:
      a2[0]=a1[0]
      a2[1]=a1[1]
    a1[0]=_a
    a1[1]=c1
  elif c1>a2[1]:
    if a1[0]!=_a:
      a2[0]=_a
      a2[1]=c1

  _b=l2[0]
  c2=1
  for x in l2[1:]:
    if _b==x:
      c2+=1
    else:
      if c2>b1[1]:
        if b1[0]!=l2[0]:
          b2[0]=b1[0]
          b2[1]=b1[1]
        b1[0]=_b
        b1[1]=c2
      elif c2>b2[1]:
        if b1[0]!=_b:
          b2[0]=_b
          b2[1]=c2
      _b=x
      c2=1
  if c2>b1[1]:
    if b1[0]!=l2[0]:
      b2[0]=b1[0]
      b2[1]=b1[1]
    b1[0]=_b
    b1[1]=c2
  elif c2>b2[1]:
    if b1[0]!=_b:
      b2[0]=_b
      b2[1]=c2

  if a1[0]!=b1[0]:
    return len(l1)-a1[1]+len(l2)-b1[1]
  else:
    return min(len(l1)-a1[1]+len(l2)-b2[1],len(l1)-a2[1]+len(l2)-b1[1])

# main()
print(main())
