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
  n,k=LI()
  r,s,p=LI()
  t=S()

  dp=[[0 for _ in range(n+1)]for __ in range(3)]

  for i in range(n):
    hyoka=t[i]

    dp[0][i+1]=max(dp[0][i],dp[1][i],dp[2][i])
    dp[1][i+1]=max(dp[0][i],dp[1][i],dp[2][i])
    dp[2][i+1]=max(dp[0][i],dp[1][i],dp[2][i])

    if i-k<0:
      if hyoka=='s':
        dp[0][i+1]+=r
      elif hyoka=='p':
        dp[1][i+1]+=s
      else:
        dp[2][i+1]+=p
    else:
      if hyoka=='s':
        if not (dp[0][i+1-k]>dp[1][i+1-k] and dp[0][i+1-k]>dp[2][i+1-k]):
          dp[0][i+1]+=r
      elif hyoka=='p':
        if not (dp[1][i+1-k]>dp[2][i+1-k] and dp[1][i+1-k]>dp[0][i+1-k]):
          dp[1][i+1]+=s
      else:
        if not (dp[2][i+1-k]>dp[0][i+1-k] and dp[2][i+1-k]>dp[1][i+1-k]):
          dp[2][i+1]+=p

  # for x in dp:
  #   print(x)
  
  return max(dp[0][n],dp[1][n],dp[2][n])

# main()
print(main())
