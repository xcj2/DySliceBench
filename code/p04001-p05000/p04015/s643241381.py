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
  n,a=LI()
  l=LI()

  dp=[[[0]*51 for _ in range(2501)] for __ in range(n+1)]
  dp[0][0][0]=1
  for i in range(n):
    nd=l[i]
    for j in range(2500):
      for k in range(50):
        ni=i+1
        nj=j
        nk=k

        dp[ni][nj][nk]+=dp[i][j][k]

        nj+=nd
        nk+=1

        if nj>2500:
          continue

        dp[ni][nj][nk]+=dp[i][j][k]

  # print(dp[2][9][1])
  # print(dp[3][9][1])
  # print(dp[4][9][1])

  ans=0
  for j in range(2501):
    for k in range(1,51):
      if j%k!=0:
        continue
      if j//k==a and dp[n][j][k]>0:
        ans+=dp[n][j][k]

  return ans

# main()
print(main())
