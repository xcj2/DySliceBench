# D問題
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

# nCr
def nCr(n,r):
  return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))

def main():
  n,k=LI()

  # 隙間
  a=n-k+1

  for i in range(1,k+1):
    if a<i or k-1<i-1:
      print(0)
    else:
      print(nCr(a,i)*nCr(k-1,i-1)%mod)

main()
