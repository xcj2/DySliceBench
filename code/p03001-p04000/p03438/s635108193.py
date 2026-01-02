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
  n=I()
  a=LI()
  b=LI()

  sm1=sum(a)
  sm2=sum(b)

  cnt=sm2-sm1
  need=0
  for i in range(n):
    need+=max(0,(b[i]-a[i]+1)//2)

  if cnt<need:
    return 'No'
  return 'Yes'

# main()
print(main())
