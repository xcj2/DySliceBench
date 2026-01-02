import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

# N=pb+r

def main():
  n,k=LI()
  ans=0

  for b in range(1,n+1):
    if b<k:
      continue

    ans+=(n//b)*(b-k)+max(0,n%b-k+1)

  if k==0:
    ans-=n
  return ans

# main()
print(main())
