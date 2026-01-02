import queue as qu
def BFS(connectinons:list,N):
    bfs_connections=[[] for _ in range(N)]
    reverse_connections=[[] for _ in range(N)]


    for A,B,_ in connectinons:
        bfs_connections[A].append(B)
        reverse_connections[B].append(A)
    
    reachable= [False]*N
    rev_reachable=[False]*N

    q = qu.Queue()
    q.put(0)

    while not q.empty():
        node = q.get()
        if reachable[node]:
            continue
        reachable[node]=True

        for B in bfs_connections[node]:
            q.put(B)
    
    q = qu.Queue()
    q.put(N-1)

    while not q.empty():
        node = q.get()
        if rev_reachable[node]:
            continue
        rev_reachable[node]=True

        for B in reverse_connections[node]:
            q.put(B)

    use=set()
    for i in range(N):
        if reachable[i] and rev_reachable[i]:
            use.add(i)
        
    return [[a,b,c] for a,b,c in connectinons if a in use and b in use]









def b_ford(connections:list,N):
    inf=float('inf')
    cost =[inf]*N
    cost[0]=0
    newchanged = set()
    oldchanged = set()

    for i in range(N):
        oldchanged=newchanged
        newchanged= set()
        for A,B,C in connections:
            if cost[A]+C < cost[B]:
                newchanged.add(B)
                cost[B]=cost[A]+C
        
        if not newchanged:
            if cost[-1] > 0:
                print(0)
            else:
                print(-cost[-1])
            return
    print(-1)







def resolve():
    N,M,P = map(int,input().split())
    
    connections = []
    for i in range(M):
        A,B,C = map(int,input().split())
        
        connections.append([A-1,B-1,P-C])
    #print(connections)
    connections = BFS(connections,N)
    #print(connections)
    b_ford(connections,N)

resolve()