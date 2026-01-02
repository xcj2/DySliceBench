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
  s=S()
  n=len(s)

  dp=[[0]*13 for _ in range(n+1)]
  dp[0][0]=1
  for i in range(n):
    if s[i]=='?':
      for j in range(10):
        for k in range(13):
          dp[i+1][(k*10+j)%13]+=dp[i][k]
    
    else:
      a=int(s[i])
      for j in range(13):
        dp[i+1][(j*10+a)%13]+=dp[i][j]

    for j in range(13):
      dp[i+1][j]%=mod

  return dp[n][5]

# main()
print(main())
