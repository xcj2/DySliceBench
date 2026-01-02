import sys
from collections import deque
sys.setrecursionlimit(10**7)
n=int(input())
l=[list(input()) for i in range(n)]
colors = [0 for i in range(n)]
es=[[] for i in range(n)]
Edges=es
for i in range(n):
  for j in range(n):
    if l[i][j]=='1':
      es[i].append(j)
def dfs(v,color):
    colors[v] = color
    for to in es[v]:
        if colors[to] == color:
            return False
        if colors[to] == 0 and not dfs(to, -color):
            return False
    return True
 
def is_bipartite():
    return dfs(0,1)
if is_bipartite()==0:
  print(-1)
  sys.exit()


def bfs(v):
    Visited=[False]*n
    q=deque()
    q.append((v,0))
    Visited[v]=True
    ret=(v,0)
    while q:
        fr,dist=q.popleft()
        if ret[1]<dist:
            ret=(fr,dist)
        for to in Edges[fr]:
            if not Visited[to]:
                Visited[to]=True
                q.append((to,dist+1))
    return ret

ans=[]
for i in range(n):
  ans.append(bfs(i)[1])
print(max(ans)+1)