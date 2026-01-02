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
  h,w=LI()
  s=[S() for _ in range(h)]

  L=[[0 for _ in range(w)]for __ in range(h)]
  R=[[0 for _ in range(w)]for __ in range(h)]
  D=[[0 for _ in range(w)]for __ in range(h)]
  U=[[0 for _ in range(w)]for __ in range(h)]

  for i in range(h):
    for j in range(w):
      if s[i][j]=='#':
        L[i][j]=0
        U[i][j]=0
        continue

      if i==0:
        U[i][j]=1
      else:
        U[i][j]=U[i-1][j]+1

      if j==0:
        L[i][j]=1
      else:
        L[i][j]=L[i][j-1]+1

  for i in range(h)[::-1]:
    for j in range(w)[::-1]:
      if s[i][j]=='#':
        R[i][j]=0
        D[i][j]=0
        continue

      if i==h-1:
        D[i][j]=1
      else:
        D[i][j]=D[i+1][j]+1

      if j==w-1:
        R[i][j]=1
      else:
        R[i][j]=R[i][j+1]+1

  ans=0
  # print(R,L,D,U)
  for i in range(h):
    for j in range(w):
      ans=max(ans,R[i][j]+L[i][j]+U[i][j]+D[i][j]-3)

  return ans

# main()
print(main())
