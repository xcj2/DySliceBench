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
  n=I()
  q=collections.deque()
  for i in range(1,10):
    q.append(i)

  while q:
    a=q.popleft()
    n-=1

    if n==0:
      return a

    _a=a%10
    for i in range(max(0,_a-1),min(10,_a+2)):
      b=int(str(a)+str(i))
      q.append(b)

# main()
print(main())
