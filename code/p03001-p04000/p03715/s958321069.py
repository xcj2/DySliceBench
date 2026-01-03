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
  h,w=LI()

  ans=inf
  for i in range(h+1):
    a=i*w
    b=(h-i+1)//2*w
    c=(h-i)//2*w
    ans=min(ans,max(a,b,c)-min(a,b,c))

    a=i*w
    b=(h-i)*((w+1)//2)
    c=(h-i)*(w//2)
    ans=min(ans,max(a,b,c)-min(a,b,c))

  for i in range(w+1):
    a=i*h
    b=(w-i+1)//2*h
    c=(w-i)//2*h
    ans=min(ans,max(a,b,c)-min(a,b,c))

    a=i*h
    b=(w-i)*((h+1)//2)
    c=(w-i)*(h//2)
    ans=min(ans,max(a,b,c)-min(a,b,c))

  return ans

# main()
print(main())
