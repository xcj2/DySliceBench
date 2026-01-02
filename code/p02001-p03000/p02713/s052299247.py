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

# GCD -- START --
def gcd(x,y):
  while y:
    x,y=y,x%y
  return x
# GCD --- END ---

def main():
  k=I()

  ans=0
  for i in range(1,k+1):
    for j in range(1,k+1):
      for l in range(1,k+1):
        ans+=gcd(gcd(i,j),l)

  return ans

# main()
print(main())
