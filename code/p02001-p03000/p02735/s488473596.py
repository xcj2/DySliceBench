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
  h,w=LI()

  l=[]
  l.append('.'*(w+1))
  for _ in range(h):
    x='.'
    x+=S()
    l.append(x)

  dp=[[inf]*(w+10) for _ in range(h+10)]
  if l[1][1]=='#':
    dp[1][1]=1
  else:
    dp[1][1]=0

  for i in range(1,h+1):
    for j in range(1,w+1):
      if i==1 and j==1:
        continue
      if l[i][j]=='#':
        if l[i-1][j]=='.':
          dp[i][j]=min(dp[i][j],dp[i-1][j]+1)
        else:
          dp[i][j]=min(dp[i][j],dp[i-1][j])
        if l[i][j-1]=='.':
          dp[i][j]=min(dp[i][j],dp[i][j-1]+1)
        else:
          dp[i][j]=min(dp[i][j],dp[i][j-1])
      else:
        dp[i][j]=min(dp[i-1][j],dp[i][j-1])

  # print(dp)
  
  return dp[h][w]

# main()
print(main())
