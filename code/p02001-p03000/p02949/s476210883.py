import sys
sys.setrecursionlimit(10**4)
def input():
	return sys.stdin.readline()[:-1]

class BellmanFord():
	def __init__(self, adj, start, size):
		self.adj = adj
		self.start = start
		self.size = size
		self.dist = [10**30 for _ in range(self.size)]
		self.dist[self.start] = 0

	def solve(self):
		for _ in range(self.size-1):
			for x in range(self.size):
				for y, w in self.adj[x]:
					if s_reachable[x] and s_reachable[y] and g_reachable[x] and g_reachable[y]:
						if self.dist[y] > self.dist[x] + w:
							self.dist[y] = self.dist[x] + w
		for x in range(self.size):
			for y, w in self.adj[x]:
				if s_reachable[x] and s_reachable[y] and g_reachable[x] and g_reachable[y]:
					if self.dist[y] > self.dist[x] + w:
						return False

		return True

	def GetDistance(self, goal):
		return self.dist[goal]

n, m, p = map(int, input().split())
adj = [[] for _ in range(n)]
adj_rev = [[] for _ in range(n)]

for _ in range(m):
	a, b, c = map(int, input().split())
	adj[a-1].append((b-1, -c+p))
	adj_rev[b-1].append(a-1)

s_reachable = [False for _ in range(n)]
s_reachable[0] = True
g_reachable = [False for _ in range(n)]
g_reachable[n-1] = True

def dfs_s(x):
	for v, w in adj[x]:
		if not s_reachable[v]:
			s_reachable[v] = True
			dfs_s(v)
	return

def dfs_g(x):
	for v in adj_rev[x]:
		if not g_reachable[v]:
			g_reachable[v] = True
			dfs_g(v)
	return

dfs_s(0)
dfs_g(n-1)

bf = BellmanFord(adj, 0, n)
if not bf.solve():
	print(-1)
else:
	print(max(-bf.GetDistance(n-1), 0))