import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m,p=map(int,input().split())
    E=[[] for _ in range(n)]
    R=[[] for _ in range(n)]
    edges=[]
    for _ in range(m):
        a,b,c=map(int,input().split())
        a-=1; b-=1
        E[a].append(b)
        R[b].append(a)
        edges.append((a,b,p-c))

    state=[0]*n

    def dfs(v):
        if(state[v]&1): return
        state[v]+=1
        for nv in E[v]: dfs(nv)
    dfs(0)

    def rdfs(v):
        if(state[v]&2): return
        state[v]+=2
        for nv in R[v]: rdfs(nv)
    rdfs(n-1)

    dist=[INF]*n
    dist[0]=0
    for k in range(n):
        for a,b,w in edges:
            if(state[a]!=3 or state[b]!=3): continue
            if(dist[b]>dist[a]+w):
                dist[b]=dist[a]+w
                if(k==n-1):
                    print(-1)
                    return
    print(max(-dist[-1],0))
resolve()