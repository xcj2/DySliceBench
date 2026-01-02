from itertools import product

class FloydWarshall:
    def __init__(self, N):
        self.N = N # #vertices
        self.E = [[] for _ in range(N)]

    def add_edge(self, init, end, weight, undirected=False):
        self.E[init].append((end, weight))
        if undirected: self.E[end].append((init, weight))
    
    def distance(self):
        INF = float('inf')
        self.dist = [[INF] * self.N for _ in range(self.N)] # dist[s][t]: the distance of vertex t from s
        self.prev = [[-1] * self.N for _ in range(self.N)] # prev[s][t]: the previous vertex of vertex t on a shortest path from s
        # initialize
        for v in range(self.N):
            self.dist[v][v] = 0; self.prev[v][v] = -1
            for u, c in self.E[v]: self.dist[v][u] = c; self.prev[v][u] = v
        # update
        for k in range(self.N):        
            for i, j in product(range(self.N), repeat=2):
                temp = self.dist[i][k] + self.dist[k][j]
                if self.dist[i][j] > temp: self.dist[i][j] = temp; self.prev[i][j] = self.prev[k][j]
        for v in range(self.N):
            if self.dist[v][v] < 0: return None # There exists a negative cycle
        return self.dist
    
    def shortest_path(self, s, t):
        P = []
        prev_s = self.prev[s]
        while True:
            P.append(t)
            t = prev_s[t]
            if t == -1: break
            elif t == P[0]: P.append(t); break
        return P[::-1]

INF = float('inf')
N, M = map(int, input().split())
fw = FloydWarshall(N)
for _ in range(M):
    a, b, c = map(int, input().split())
    fw.add_edge(a, b, c)
dist = fw.distance()
if dist is None: print('NEGATIVE CYCLE')
else:
    for dst in dist: print(*[d if d != INF else 'INF' for d in dst])
