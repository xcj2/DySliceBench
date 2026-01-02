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

  l=[]
  for i in range(m):
    a,b=LI()
    l.append([i,a,b,0])

  l=sorted(l,key=lambda x:[x[1],x[2]])

  a=l[0][1]
  b=1
  l[0][3]=b

  for i in range(1,len(l)):
    if a==l[i][1]:
      b+=1
    else:
      a=l[i][1]
      b=1
    l[i][3]=b

  l=sorted(l,key=lambda x:x[0])

  for x in l:
    print(str(x[1]).zfill(6)+str(x[3]).zfill(6))

main()
