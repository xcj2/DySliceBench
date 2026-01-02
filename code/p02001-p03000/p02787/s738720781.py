import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=998244353
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
# def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  p=20010
  h,n=LI()
  a=[]
  b=[]

  for _ in range(n):
    x,y=LI()
    a.append(x)
    b.append(y)

  dp=[[inf]*p for _ in range(n+1)]
  dp[0][0]=0

  for i in range(n):
    for j in range(p-5):
      dp[i+1][j]=min(dp[i+1][j],dp[i][j])
      if j+a[i]<p:
        dp[i+1][j+a[i]]=min(dp[i+1][j+a[i]],dp[i+1][j]+b[i])

  # print(dp)
  ans=inf
  for i in range(h,20010):
    ans=min(ans,dp[n][i])
  return ans

# main()
print(main())
