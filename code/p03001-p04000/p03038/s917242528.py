import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  n,m=LI()
  l=LI()

  l.sort()
  sm=sum(l)

  l3=[]
  for i in range(m):
    a,b=LI()
    l3.append([b,a])
  l3=sorted(l3,key=lambda x:x[0],reverse=True)

  n2=0
  for x in l3:
    n2+=x[1]

  # if n>n2:
  i=0
  i2=0
  while True:
    if i>n-1:
      break
    if i2>m-1:
      break

    a,b=l3[i2]
    while True:
      if i>n-1:
        break
      if i2>m-1:
        break

      if b==0:
        i2+=1
        break

      x=l[i]
      if x<a:
        sm+=a-x
        b-=1
        i+=1
      else:
        i2+=1
        break

  print(sm)

main()
