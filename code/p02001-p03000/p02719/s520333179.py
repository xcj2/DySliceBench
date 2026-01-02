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

  a=n//k
  n-=(a*k)

  a=n
  b=abs(n-k)
  f1=f2=False
  for i in range(100):
    n=abs(n-k)
    if a==n:
      f1=True
    if b==n:
      f2=True

    if f1 and f2:
      return min(a,b)

# main()
print(main())
