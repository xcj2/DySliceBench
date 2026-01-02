from collections import deque

class Edge:
	def __init__(self, t, w):
		self.to = t
		self.ew = w

class Graph:
	def __init__(self, N):
		self.nw = [-1] * N
		self.al = [[] for i in range(N)]

	def add_edge(self, fr, to, weight):
		self.al[fr].append(Edge(to, weight))
		self.al[to].append(Edge(fr, -weight))

	def dfs(self, s, used):
		self.nw[s] = 0
		q = deque([s])
		used.add(s)
		while q:
			h = q.popleft()
			for e in self.al[h]:
				if e.to in used:
					if self.nw[h] + e.ew != self.nw[e.to]:
						return False
					continue
				used.add(e.to)
				self.nw[e.to] = self.nw[h] + e.ew
				q.appendleft(e.to)
		return True


def main():
	N, M = map(int, input().split())
	graph = Graph(N)
	for i in range(M):
		l, r, d = map(int, input().split())
		graph.add_edge(l - 1, r - 1, d)

	used = set()
	for i in range(N):
		if i in used or graph.dfs(i, used):
			continue
		print("No")
		break
	else:
		print("Yes")


if __name__ == "__main__":
	main()
