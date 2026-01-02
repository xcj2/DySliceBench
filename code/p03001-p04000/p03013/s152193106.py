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
  n,m=LI()
  l=[True for _ in range(n+1)]
  for _ in range(m):
    l[I()]=False

  dp=[0 for _ in range(n+1)]
  dp[0]=1
  for i in range(n):
    for j in range(1,3):
      if i+j<=n and l[i]:
        dp[i+j]+=dp[i]

  # print(dp)
  return dp[n]%mod

# main()
print(main())
