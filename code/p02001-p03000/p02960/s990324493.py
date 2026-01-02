import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
# def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  s=list(S())[::-1]
  n=len(s)
  dp=[[0]*13 for _ in range(n+1)]

  dp[0][0]=1
  mul=1
  for i in range(n):
    for j in range(13):
      if s[i]=='?':
        for k in range(10):
          dp[i+1][(j+k*mul)%13]+=dp[i][j]
          dp[i+1][(j+k*mul)%13]%=mod
      else:
        dp[i+1][(j+int(s[i])*mul)%13]+=dp[i][j]
        dp[i+1][(j+int(s[i])*mul)%13]%=mod
    mul*=10
    mul%=13

  return dp[n][5]%mod

# main()
print(main())
