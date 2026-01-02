import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

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
  field=[list(S()) for _ in range(h)]
  u=[[0]*w for _ in range(h)]
  d=[[0]*w for _ in range(h)]
  l=[[0]*w for _ in range(h)]
  r=[[0]*w for _ in range(h)]

  for i in range(h):
    for j in range(w):
      if field[i][j]=='#':
        u[i][j]=0
        l[i][j]=0
      else:
        if i!=0:
          u[i][j]=u[i-1][j]+1
        else:
          u[i][j]=1
        if j!=0:
          l[i][j]=l[i][j-1]+1
        else:
          l[i][j]=1

  for i in range(h)[::-1]:
    for j in range(w)[::-1]:
      if field[i][j]=='#':
        d[i][j]=0
        r[i][j]=0
      else:
        if i!=h-1:
          d[i][j]=d[i+1][j]+1
        else:
          d[i][j]=1
        if j!=w-1:
          r[i][j]=r[i][j+1]+1
        else:
          r[i][j]=1

  ans=-inf
  for i in range(h):
    for j in range(w):
      ans=max(ans,u[i][j]+d[i][j]+l[i][j]+r[i][j]-3)

  return ans

# main()
print(main())
