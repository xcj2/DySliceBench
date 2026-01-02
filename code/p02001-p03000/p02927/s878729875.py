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
  m,d=LI()
  ans=0

  for i in range(1,m+1):
    for j in range(10,d+1):
      j=str(j)
      d1=int(j[1])
      d10=int(j[0])

      if d1<2:
        continue
      if d10<2:
        continue

      if d1*d10==i:
        # print(i,j)
        ans+=1
  return ans

# main()
print(main())
