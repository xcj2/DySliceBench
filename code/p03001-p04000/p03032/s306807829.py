import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=1000000007
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  n,k=LI()
  l=LI()

  cnt=min(n,k)
  ans=0
  for i in range(cnt+1):
    for j in range(cnt-i+1):
      q=[]
      for _i in range(i):
        heapq.heappush(q,l[_i])

      for _j in range(j):
        heapq.heappush(q,l[-(_j+1)])

      ln=len(q)
      for _ in range(min(k-i-j,ln)):
        x=heapq.heappop(q)
        if x>0:
          q.append(x)
          break
      # print(q)
      ans=max(ans,sum(q))

  return ans

# main()
print(main())
