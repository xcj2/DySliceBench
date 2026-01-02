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

# GCD
def gcd(x,y):
  while y:
    x,y=y,x%y
  return x

# LCM
def lcm(x,y):
  return x*y/gcd(x,y)

def main():
  a,b,c,d=LI()
  ans=b-a+1
  ans-=b//c+(-a//c)+1
  ans-=b//d+(-a//d)+1
  ans+=b//int(lcm(c,d))+(-a//int(lcm(c,d)))+1
  return ans

# main()
print(main())
