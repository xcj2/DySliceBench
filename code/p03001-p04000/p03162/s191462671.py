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
  n=I()
  l=[LI() for _ in range(n)]

  dp=[[0 for _ in range(n+1)]for __ in range(3)]

  for i in range(n):
    for j in range(3):
      dp[j][i+1]=max(dp[(j+1)%3][i],dp[(j+2)%3][i])+l[i][j]
  return max(dp[0][n],dp[1][n],dp[2][n])

# main()
print(main())
