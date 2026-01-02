import sys,collections
V,E = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
#sdw = [[src1 dist1 d1][src1 dist1 d1]...]# vect source1 -> distance1 distances
INF = float("inf")

st = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(E)) # multi line with multi param

G = [[] for _ in range(V)]

for s,t in st:
    G[s].append(t)

visited = set()
indeg = [0]*V
ret = []
def bfs(s):
    q = collections.deque([s])
    visited.add(s)
    while q:
        u = q.popleft()
        ret.append(u)
        for v in G[u]:
            indeg[v] -= 1
            if indeg[v] == 0 and not v in visited:
                visited.add(v)
                q.append(v)

def topologicalSort_bfs():
    for a in G:
        for t in a:
            indeg[t] += 1
    #print(G,indeg)
    for i in range(V):
        if indeg[i] == 0 and not i in visited:
            bfs(i)

def dfs(s):
    #print("s:",s)
    if s in visited:
        return
    for e in G[s]:
        dfs(e)
    ret.append(s)
    visited.add(s)

def topologicalSort_dfs():
    for i in range(V):
        dfs(i)
    ret.reverse()

topologicalSort_bfs()
#topologicalSort_dfs()
print(*ret,sep='\n')

