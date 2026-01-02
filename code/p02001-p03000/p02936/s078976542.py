from collections import deque
from collections import defaultdict

def getlist():
	return list(map(int, input().split()))

class Graph(object):

    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, a, b):
        self.graph[a].append(b)

G = Graph()

N, Q = getlist()
for i in range(N - 1):
	a, b = getlist()
	G.add_edge(a, b)
	G.add_edge(b, a)

plus = [0] * (N + 1)
for i in range(Q):
	p, x = getlist()
	plus[p] += x

q = deque([]) 
ans = [0] * N
visit = [-1] * (N + 1)
visit[1] = 1
q.append(1)
while q:
	m = q.pop()
	visit[m] = 1
	ans[m - 1] += plus[m]
	x = ans[m - 1]
	for i in G.graph[m]:
		if visit[i] == -1:
			q.append(i)
			ans[i - 1] += x

print(" ".join(list(map(str, ans))))