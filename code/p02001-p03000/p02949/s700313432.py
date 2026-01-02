def connect_dfs(N,E,start):
    connect = {start}
    q = [start]
    while q:
        i = q.pop()
        for j in E[i]:
            if j in connect:continue
            connect.add(j)
            q.append(j)
    return connect

def remove_Edge(N,Ef,Eb,start,goal):
    v = connect_dfs(N,Ef,start) & connect_dfs(N,Eb,goal)
    for i in range(N):
        if i in v:continue
        for j in Eb[i]:
            Ef[j].pop(i)

def Bellman_Ford(N,E,start,INFTY=10**18):
    def update(dist,N,E,start):
        done = [False]*N
        done[start] = True
        q = [start]
        d = dist[:]
        while q:
            i = q.pop()
            di = d[i]
            for j,c in E[i].items():
                d[j] = min(d[j],d[i]+c)
                if not done[j]:
                    q.append(j)
                    done[j] = True
        return d
    #
    d = [INFTY]*N
    d[start] = 0
    for _ in range(N-1):
        d = update(d,N,E,start)
    if d!=update(d,N,E,start): return None
    else: return d

N,M,P = map(int,input().split())
ABC = [list(map(int,input().split())) for _ in [0]*M]

Ef = [{} for _ in [0]*N]
Eb = [{} for _ in [0]*N]
INFTY = 10**18
for a,b,c in ABC:
    Ef[a-1][b-1] = min(P-c,Ef[a-1].get(b-1,INFTY))
    Eb[b-1][a-1] = min(P-c,Eb[b-1].get(a-1,INFTY))
    
remove_Edge(N,Ef,Eb,0,N-1)
d = Bellman_Ford(N,Ef,0)

if d==None:ans=-1
else:ans = max(0,-d[-1])
print(ans)