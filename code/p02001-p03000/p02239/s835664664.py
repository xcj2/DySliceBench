import collections,sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
n = I()
ukv = [LI() for _ in range(n)]
graph = {i:collections.deque() for i in range(1,n+1)} #1_indexed
for x in ukv:
    u,k,*v = x
    for y in v:
        graph[u].append(y)
seen = [0]*(n+1) #1_indexed
min_dist = [-1]*(n+1) #1_indexed
queue = collections.deque() #頂点NOを入れておく
def bfs():
    seen[1] = 1
    queue.append(1)
    min_dist[1] = 0
    while queue:
        q_NO = queue.popleft()
        q_dist = min_dist[q_NO]
        if not graph[q_NO]:
            continue
        g = graph[q_NO]
        for _ in range(len(g)):
            g_NO = g.popleft()
            if seen[g_NO]:
                continue
            seen[g_NO] = 1
            queue.append(g_NO)
            min_dist[g_NO] = q_dist+1
bfs()
for i,ans in enumerate(min_dist[1:],1):
    print(i,ans)
