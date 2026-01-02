import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

nmax=50
graph=[[False]*nmax for _ in range(nmax)]
visited=[False]*nmax

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
  a=[]
  b=[]
  for _ in range(m):
    _a,_b=LI()
    a.append(_a-1)
    b.append(_b-1)
    graph[_a-1][_b-1]=True
    graph[_b-1][_a-1]=True

  ans=0
  for i in range(m):
    graph[a[i]][b[i]]=False
    graph[b[i]][a[i]]=False

    for j in range(n):
      visited[j]=False

    dfs(n,j)

    bridge=False
    for j in range(n):
      if visited[j]==False:
        bridge=True
    if bridge:
      ans+=1

    graph[a[i]][b[i]]=True
    graph[b[i]][a[i]]=True

  return ans

# main()
print(main())
