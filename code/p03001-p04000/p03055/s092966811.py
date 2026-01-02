from collections import defaultdict
from collections import deque

def getlist():
	return list(map(int, input().split()))

class Graph(object):

    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, a, b):
        self.graph[a].append(b)


class breadth(object):
    def __init__(self, graph, s):
        self.g = graph.graph
        self.dist = defaultdict(lambda: float('inf'))
        self.dist[s] = 0
        self.visit = ["no" for i in range(len(graph) + 1)]
        self.visit[s] = "yes"

        self.Q = deque()
        self.Q.append([self.dist[s], s])

        while self.Q:
            dist_u, u = self.Q.popleft()
            for v in self.g[u]:
                if self.visit[v] == "yes":
                    continue
                else:
                    self.dist[v] = dist_u + 1
                    self.visit[v] = "yes"
                    self.Q.append([self.dist[v], v])


N = int(input())
if N == 1:
	print("First")
else:
	g_a = Graph()
	for i in range(N - 1):
		a, b = getlist()
		g_a.add_edge(a, b)
		g_a.add_edge(b, a)
	
	s = 1
	E = breadth(g_a, s)
	x = 0
	for i in E.dist:
		if E.dist[i] > x:
			x = E.dist[i]
			y = i
	F = breadth(g_a, y)
	x = 0
	for i in F.dist:
		if F.dist[i] > x:
			x = F.dist[i]
			y = i

	if x % 3 == 0 or x % 3 == 2:
		print("First")
	else:
		print("Second")
