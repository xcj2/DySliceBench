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
  l=LI()

  l.sort()
  a=l[0]
  l2=[]
  c=1
  for x in l[1:]:
    if a==x:
      c+=1
    else:
      l2.append([a,c])
      c=1
      a=x
  l2.append([a,c])

  l2=sorted(l2,key=lambda x:x[1])

  ans=0
  for i in range(len(l2)-m):
    ans+=l2[i][1]

  return ans

print(main())
