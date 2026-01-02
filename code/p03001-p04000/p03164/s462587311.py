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
  n,W=LI()
  dp=[[inf]*100100 for _ in range(n+1)]
  dp[0][0]=0

  w=[]
  v=[]
  for _ in range(n):
    a,b=LI()
    w.append(a)
    v.append(b)

  for i in range(n):
    for j in range(100100):
      dp[i+1][j]=min(dp[i+1][j],dp[i][j])

      if j+v[i]<100100:
        dp[i+1][j+v[i]]=min(dp[i+1][j+v[i]],dp[i][j]+w[i])

  ans=0
  for i in range(100100):
    x=dp[n][i]
    if x<=W:
      ans=i

  return ans

# main()
print(main())
