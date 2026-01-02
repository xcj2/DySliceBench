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

# GCD -- START --
def gcd(x,y):
  while y:
    x,y=y,x%y
  return x
# GCD --- END ---

# LCM -- START --
def lcm(x,y):
  return x*y//gcd(x,y)
# LCM --- END ---

def main():
  n,m=LI()
  s=S()
  t=S()
  a=lcm(n,m)

  x={}
  for i in range(n):
    x[i*(a//n)]=s[i]

  # print(x)

  for i in range(m):
    if i*(a//m) in x:
      if t[i]!=x[i*(a//m)]:
        return -1

  return a

# main()
print(main())
