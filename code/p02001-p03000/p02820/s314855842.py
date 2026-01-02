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
  n,k=LI()
  r,s,p=LI()
  t=S()

  dp=[[0]*3 for _ in range(n+1)]
  for i in range(n):
    a=t[i]
    b=max(dp[i])
    for j in range(3):
      dp[i+1][j]=b
    if i+1<=k:
      if a=='r':
        dp[i+1][2]+=p
      elif a=='s':
        dp[i+1][0]+=r
      else:
        dp[i+1][1]+=s

    else:
      _a,_b,_c=dp[i+1-k]
      if a=='r':
        if not (_c>_a and _c>_b):
          dp[i+1][2]+=p
      elif a=='s':
        if not (_a>_b and _a>_c):
          dp[i+1][0]+=r
      else:
        if not (_b>_a and _b>_c):
          dp[i+1][1]+=s

  # print(dp)
  return max(dp[n])

# main()
print(main())
