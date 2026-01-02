import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  n,k=LI()
  h=LI()
  h=[0]+h
  h+=[inf]*k

  dp=[inf]*114514
  dp[1]=0
  for i in range(1,n):
    for j in range(1,k+1):
      dp[i+j]=min(dp[i+j],dp[i]+abs(h[i+j]-h[i]))
  # print(dp[:10])
  return dp[n]

# main()
print(main())
