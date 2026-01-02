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
  _l=LI()

  l=[]
  for i,x in enumerate(_l):
    l.append(x-(i+1))

  l.sort()
  if n%2==1:
    x=l[n//2]
  else:
    x=(l[n//2]+l[n//2-1])//2

  ans=0
  for y in l:
    ans+=abs(y-x)

  return ans

# main()
print(main())
