from collections import defaultdict
import queue

def getlist():
	return list(map(int, input().split()))

class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, a, b, w):
        self.graph[a].append([b, w])
        self.graph[b].append([a,w])

    def get_nodes(self):
        return self.graph.keys()

class BFS(object):
    def __init__(self, graph, N):
        self.g = graph.graph
        self.dist = [0] * (N + 1)
        self.visit = [0] * (N + 1)
        self.Q = queue.Queue()
        self.visit[1] = 1
        self.Q.put(1)

        while not self.Q.empty():
            v = self.Q.get()
            for i, w in self.g[v]:
            	if self.visit[i] == 0:
            		self.dist[i] = self.dist[v] + w
            		self.Q.put(i)
            		self.visit[i] = 1

    def weight(self):
        return self.dist

N = int(input())
G = Graph()
for i in range(N - 1):
	u, v, w = getlist()
	G.add_edge(u, v, w)
XX = BFS(G, N)
ans = XX.weight()
for i in range(1, N + 1):
	if ans[i] % 2 == 0:
		print(0)
	else:
		print(1)
