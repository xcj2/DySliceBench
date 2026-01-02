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

limit=50
graph=[[False]*limit for _ in range(limit)]
visited=[False]*limit

def dfs(n,v):
  visited[v]=True
  for v2 in range(n):
    if graph[v][v2]==False:
      continue
    if visited[v2]:
      continue
    dfs(n,v2)

def main():
  n,m=LI()
  a=[[] for _ in range(n*n)]
  b=[[] for _ in range(n*n)]
  for i in range(m):
    _a,_b=LI()
    _a-=1
    _b-=1
    a[i]=_a
    b[i]=_b
    graph[_a][_b]=True
    graph[_b][_a]=True

  ans=0
  for i in range(m):
    graph[a[i]][b[i]]=False
    graph[b[i]][a[i]]=False

    for j in range(n):
      visited[j]=False
    dfs(n,0)
    no_visited=False
    for j in range(n):
      if visited[j]==False:
        no_visited=True
    if no_visited:
      ans+=1
    graph[a[i]][b[i]]=True
    graph[b[i]][a[i]]=True

  return ans

# main()
print(main())
