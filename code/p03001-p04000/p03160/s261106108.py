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
  n=I()
  h=LI()
  h.append(inf)

  dp=[inf]*114514
  dp[1]=0
  for i in range(1,n):
    dp[i+1]=min(dp[i+1],dp[i]+abs(h[i]-h[i-1]))
    dp[i+2]=min(dp[i+2],dp[i]+abs(h[i+1]-h[i-1]))
  return dp[n]

# main()
print(main())
