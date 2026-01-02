# https://atcoder.jp/contests/arc026/tasks/arc026_2
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
  n=I()
  ans=''
  if n==0:
    return 0

  while True:
    if abs(n)==0:
      return ans

    if n%2==0:
      ans='0'+ans
    else:
      ans='1'+ans
    n//=2
    n*=(-1)

# main()
print(main())
