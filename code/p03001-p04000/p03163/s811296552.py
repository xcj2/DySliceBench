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
  n,W=LI()
  w=[]
  v=[]
  dp=[[0 for _ in range(W+1)] for __ in range(n+1)]
  for _ in range(n):
    a,b=LI()
    w.append(a)
    v.append(b)

  for i in range(n)[::-1]:
    for j in range(W+1):

      if j<w[i]:
        dp[i][j]=dp[i+1][j]

      else:
        dp[i][j]=max(dp[i+1][j],dp[i+1][j-w[i]]+v[i])

  return dp[0][W]

# main()
print(main())
