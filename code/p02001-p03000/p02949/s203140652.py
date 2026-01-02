INF = 10 ** 15
MOD = 10 ** 9 + 7

def beruman(n,X,edges,start = 0,negative_loop = False):
    ans = False #startを含む負の閉路が存在するか
    dist = [INF] * n
    dist[start] = 0

    for i in range(X):
        update = False
        for a,b,c in edges:
            if dist[a] != INF and dist[b] > dist[a] + c:
                dist[b] = dist[a] + c
                update = True

        if not update:
            break
        if i == X - 1:
            ans = True
    
    if negative_loop:
        return dist,ans
    else:
        return dist

def dfs(G,can_reach,start):
    stack = [start]
    can_reach[start] = True
    while stack:
        v = stack.pop()
        for e in G[v]:
            if can_reach[e]:
                continue
            stack.append(e)
            can_reach[e] = True
    return can_reach

def main():
    N,M,P = map(int,input().split())
    edges = []
    G = [[] for _ in range(N)]
    G_inv = [[] for _ in range(N)]
    for _ in range(M):
        a,b,c = map(int,input().split())
        a -= 1
        b -= 1
        edges.append((a,b,P - c))
        G[a].append(b)
        G_inv[b].append(a)
    
    can_reach_from_start = [False] * N
    can_reach_from_goal = [False] * N
    dfs(G,can_reach_from_start,0)
    dfs(G_inv,can_reach_from_goal,N - 1)
    in_route = [False] * N
    X = 0
    for i in range(N):
        if can_reach_from_goal[i] and can_reach_from_start[i]:
            in_route[i] = True
            X += 1
        
    edge = []
    for a,b,c in edges:
        if in_route[a] and in_route[b]:
            edge.append((a,b,c))

    dist,flag = beruman(N,X,edge,0,True)
    if flag:
        print(-1)
    else:
        print(max(-dist[-1],0))
if __name__ == '__main__':
    main()
