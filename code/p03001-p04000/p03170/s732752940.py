import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  n,k=LI()
  l=LI()

  # 負け：0 勝ち：1
  dp=[0]*(k+1)
  for i in range(k+1):
    for x in l:
      y=i+x

      if y<=k:
        if dp[y]==0:
          dp[y]=abs(dp[i]-1)
  # print(dp)

  if dp[k]==1:
    return 'First'
  return 'Second'

# main()
print(main())
