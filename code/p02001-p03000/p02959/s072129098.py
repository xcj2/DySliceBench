import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  n=I()
  l1=LI()
  l2=LI()

  ans=0
  for i in range(n):
    x=l2[i]
    y=l1[i]
    if y<=x:
      ans+=y
      x-=y

      if l1[i+1]<=x:
        ans+=l1[i+1]
        l1[i+1]=0
      else:
        ans+=x
        l1[i+1]-=x

    else:
      ans+=x

  return ans

# main()
print(main())
