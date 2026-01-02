# https://atcoder.jp/contests/abc150/tasks/abc150_d
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

# LCM -- START --
def lcm(x,y):
  return x*y//gcd(x,y)
# LCM --- END ---

def f(x):
  a=0
  while x%2==0:
    x//=2
    a+=1
  return a

def main():
  n,m=LI()
  _l=LI()
  l=[x//2 for x in _l]

  t=f(l[0])
  for i in range(n):
    b=l[i]
    if t!=f(b):
      return 0
    l[i]>>=t
  m>>=t

  _lcm=1
  for x in l:
    _lcm=lcm(_lcm,x)
    if _lcm>m:
      return 0

  # print(m,_lcm)
  m//=_lcm
  return (m+1)//2

# main()
print(main())
