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

def main():
  n,m=LI()
  ans=1
  if n==1:
    return m
  for i in range(1,int(math.sqrt(m)+1)):
    if m%i==0:
      if i*n>m:
        continue
      ans=max(ans,i)
      x=m//i
      if x*n>m:
        continue
      ans=max(ans,x)

  return ans

# main()
print(main())
