# https://atcoder.jp/contests/abc054/tasks/abc054_c

import math,itertools,fractions,heapq,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

nmax=8
graph=[[False]*nmax for _ in range(nmax)]

def dfs(n,v,visited):
  all_visited=True
  for i in range(n):
    if visited[i]==False:
      all_visited=False
  if all_visited:
    return 1

  ret=0
  for i in range(n):
    if visited[i]:
      continue
    if graph[i][v]==False:
      continue
    visited[i]=True
    ret+=dfs(n,i,visited)
    visited[i]=False

  return ret

def main():
  n,m=LI()
  for _ in range(m):
    a,b=LI()
    a-=1
    b-=1
    graph[a][b]=True
    graph[b][a]=True

  visited=[False]*n
  visited[0]=True
  return dfs(n,0,visited)

# main()
print(main())
