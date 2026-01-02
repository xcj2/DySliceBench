import math,itertools,fractions,heapq,bisect,sys,queue,copy

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
  h,w=LI()
  dp=[[0]*w for _ in range(h)]
  dp[0][0]=1

  l=[S() for _ in range(h)]

  for i in range(h):
    for j in range(w):
      
      y=i-1
      x=j-1

      if y<0 and x<0:
        continue
      if l[i][j]=='#':
        continue
      if y<0:
        dp[i][j]=dp[i][j-1]
      elif x<0:
        dp[i][j]=dp[i-1][j]
      else:
        dp[i][j]=(dp[i-1][j]+dp[i][j-1])%mod

  return dp[h-1][w-1]

# main()
print(main())
