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
  l1=[LI() for _ in range(n)]
  l1.sort()
  l2=[LI() for _ in range(n)]
  l2.sort()

  check=[False for _ in range(n)]

  ans=0
  ans_list=[]
  for c,d in l2:
    _i=inf
    _b=-inf
    for i,[a,b] in enumerate(l1):
      if check[i]:
        continue

      if a<c and b<d:
        if _b<b:
          _i=i
          _b=b

    if _i!=inf:
      check[_i]=True
      ans+=1

  return ans

# main()
print(main())
