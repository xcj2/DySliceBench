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
  l=[LI() for _ in range(n)]
  l.sort(reverse=True)

  q=[]
  i=1
  ans=0
  while True:
    while True:
      if len(l)>0:
        if l[-1][0]<=i:
          a,b=l.pop()
          heapq.heappush(q,-b)
        else:
          break
      else:
        break
    if len(q)>0:
      c=heapq.heappop(q)
      ans-=c
    i+=1

    if i>m:
      break

  return ans

# main()
print(main())
