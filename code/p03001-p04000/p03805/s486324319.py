import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

nmax=8
graph=[[False for __ in range(nmax)]for _ in range(nmax)]

def dfs(v,n,visited):
  visited[v]=True

  all_visited=True
  for i in range(n):
    if visited[i]==False:
      all_visited=False
  if all_visited:
    return 1

  ret=0
  for i in range(n):
    if graph[v][i]==False:
      continue
    if visited[i]:
      continue
    visited[i]=True
    ret+=dfs(i,n,visited)
    visited[i]=False

  return ret

def main():
  n,m=LI()
  for _ in range(m):
    a,b=LI()
    graph[a-1][b-1]=True
    graph[b-1][a-1]=True

  visited=[False for _ in range(n)]
  visited[0]=True
  return dfs(0,n,visited)

# main()
print(main())
