import sys
sys.setrecursionlimit(10**7)
 
n=int(input())
l=[list(input()) for i in range(n)]
connection=[[] for i in range(n)]
for i in range(n):
  for j in range(n):
    if l[i][j]=='1':
      connection[i].append(j)
 
colors = [0]*n
def dfs(v,color):
    colors[v] = color
    for to in connection[v]:
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
  distance=[-1]*n
  distance[v]=0
  next=connection[v]
  next2=set()
  visited=[-1]*n
  visited[v]=1
  visitct=1
  ct=0
  while visitct!=n:
    ct+=1
    for i in range(len(next)):
      distance[next[i]]=ct
      visited[next[i]]=1
      visitct+=1
      for j in range(len(connection[next[i]])):
        if visited[connection[next[i]][j]]==-1:
          next2.add(connection[next[i]][j])
    next=list(next2)
    next2=set()
    
  return distance

ans=[]
for i in range(n):
  ans.append(max(bfs(i)))
print(max(ans)+1)