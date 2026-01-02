import queue

N = int(input())
L = [list(map(int,input().split())) for _ in range(N)]
V = [(i+1) for i in range(N)]
E = []
for i in range(N):
    for j in range(len(L[i])-2):
        E.append((i+1,L[i][j+2]))

class Graph:
    def __init__(self,v,e):
        self.v = v
        self.e = e
        self.v_visited = [False for _ in range(N)]
    def visited(self,v):
        self.v_visited[v-1] = True

q = queue.Queue()
g = Graph(V,E)
TS = [-1 for _ in range(N)]

def bfs(u):
    q.put(u)
    g.visited(u)
    TS[u-1] = 0
    while not q.empty():
        u = q.get()
        for v in g.v:
            if (u,v) in g.e and g.v_visited[v-1] == False:
                q.put(v)
                g.visited(v)
                TS[v-1] = TS[u-1]+1
bfs(1)

for i in range(N):
    print(i+1,TS[i])

