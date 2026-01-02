import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=1000000007
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  s=S()
  l=len(s)
  _k=I()

  dp=[[[0]*2 for _ in range(4)]for __ in range(l+1)]
  dp[0][0][0]=1

  for i in range(l):
    nd=int(s[i])
    for j in range(4):
      for k in range(2):
        for d in range(10):
          ni=i+1
          nj=j
          nk=k

          if d!=0:
            nj+=1

          if nj>_k:
            continue

          if k==0:
            if nd>d:
              nk=1
            if nd<d:
              continue

          dp[ni][nj][nk]+=dp[i][j][k]

  return dp[l][_k][0]+dp[l][_k][1]

# main()
print(main())
