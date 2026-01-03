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
    if d!=update(d,N,E,start):
        return None
    else:
        return d

def main():
    N,M = map(int,input().split())
    ABC = [list(map(int,input().split())) for _ in [0]*M]
    E = [{} for _ in [0]*N]
    Eb = [{} for _ in [0]*N]
    for a,b,c in ABC:
        E[a-1][b-1] = -c
        Eb[b-1][a-1] = c
    
    remove_Edge(N,E,Eb,0,N-1)
    d = Bellman_Ford(N,E,0)
    if d == None:
        print("inf")
    else:
        print(-d[-1])
    
main()