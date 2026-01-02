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
  n,m=LI()
  l=LI()

  sm=sum(l)
  a=sm/(4*m)

  l.sort(reverse=True)
  for x in l:
    if m<=0:
      return 'Yes'
    m-=1
    if x<a:
      return 'No'
  if m<=0:
    return 'Yes'
  return 'No'

# main()
print(main())
