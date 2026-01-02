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

def main():
  n,x,m=LI()
  ans=[x]
  d={x:x}
  y=-inf
  for i in range(n-1):
    x=x*x%m
    if x in d:
      y=x
      break
    d[x]=x
    ans.append(x)

  if y==-inf:
    return sum(ans)

  # print(ans)

  for i,x in enumerate(ans):
    if x==y:
      break

  sm=sum(ans)
  n-=len(ans)
  ans2=ans[i:]
  sm+=n//len(ans2)*sum(ans2)

  n%=len(ans2)
  for i in range(i,i+n):
    sm+=ans[i]

  return sm

# main()
print(main())
