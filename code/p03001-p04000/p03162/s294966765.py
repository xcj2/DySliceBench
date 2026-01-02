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
  n=I()
  a=[]
  b=[]
  c=[]
  for _ in range(n):
    x,y,z=LI()
    a.append(x)
    b.append(y)
    c.append(z)

  dp=[[0]*114514 for _ in range(3)]
  for i in range(1,n+1):
    dp[0][i]=max(dp[1][i-1],dp[2][i-1])+a[i-1]
    dp[1][i]=max(dp[2][i-1],dp[0][i-1])+b[i-1]
    dp[2][i]=max(dp[0][i-1],dp[1][i-1])+c[i-1]

  return max(dp[0][n],dp[1][n],dp[2][n])

# main()
print(main())
