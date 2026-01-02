import math,itertools,fractions,heapq,bisect,sys,queue,copy

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
  n,m=LI()

  if n==1:
    return m

  a=0
  for i in range(1,int(math.sqrt(m))+1):
    if m%i==0:
      if m>=i*n:
        a=max(a,i)
      if m>=m//i*n:
        a=max(a,m//i)

  return a

# main()
print(main())
