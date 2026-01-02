import sys
from collections import deque
parent=[]

def bfs(G,s,t,parent):
    N = len(G)
    visited=[False for u in range(N)]
    cola = deque()
    parent[s]=-1
    visited[s]=True
    cola.append(s)
    while cola:
        u = cola.popleft()
        for v in range(N):
            if(visited[v]==False and G[u][v]):
                cola.append(v)
                visited[v]=True
                parent[v]=u
    return visited[t]
    


def MAX_FLOW(G,s,t):
    global parent
    maxflow=0
    u,v=0,0
    GR=G
    while bfs(GR,s,t,parent):
        pathFlow=float("inf")
        v=t
        while v!=s:
            u=parent[v]
            pathFlow=min(pathFlow,GR[u][v])
            v=parent[v]
        v=t
        while v!=s:
          u=parent[v]
          GR[u][v]-=pathFlow
          GR[v][u]+=pathFlow
          v=parent[v]
        maxflow+=pathFlow
    return maxflow
        
        

def main():
    global parent
    D=[int(x) for x in sys.stdin.readline().strip().split()]
    V,E=D[0],D[1]
    G=[[0 for u in range(V)]for v in range(V)]
    for l in range(E):
        u,v,c= [int(x) for x in sys.stdin.readline().strip().split()]
        G[u][v]=c
    parent=[-1 for i in range(V)]
    print(MAX_FLOW(G,0,V-1))
main()

