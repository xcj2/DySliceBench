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

def main():
  h,n=LI()
  w=[]
  v=[]
  max_w=0
  for _ in range(n):
    _w,_v=LI()
    w.append(_w)
    v.append(_v)
    max_w=max(max_w,_w)

  dp=[[inf]*(h+10**4+1) for _ in range(n+1)]
  dp[0][0]=0
  for i in range(n):
    for j in range(h+max_w):
      if j<w[i]:
        dp[i+1][j]=dp[i][j]
      else:
        dp[i+1][j]=min(dp[i][j],dp[i+1][j-w[i]]+v[i])
  ans=inf
  for i in range(n+1):
    for j in range(h,h+max_w):
      ans=min(ans,dp[i][j])

  return ans

# main()
print(main())
