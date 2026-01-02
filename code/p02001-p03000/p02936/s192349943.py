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

cost=[0]*200010
G=[[] for _ in range(200010)]
visited=[False]*200010
visited[0]=True

def dfs(s):
  global cost
  global G
  global visited
  for e in G[s]:
    if visited[e]==False:
      cost[e]+=cost[s]
      visited[e]=True
      dfs(e)
      visited[e]=False

def main():
  global cost
  global G
  global visited
  n,q=LI()
  for _ in range(n-1):
    a,b=LI()
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)

  for i in range(q):
    p,x=LI()
    p-=1
    cost[p]+=x
  dfs(0)

  return ' '.join([str(x) for x in cost[:n]])

# main()
print(main())
