from typing import List

class UnionFind:
	def __init__(self, V: int) -> None:
		self.V: int = V
		self.pi: List[int] = [i for i in range(V)]
		self.rank: List[int] = [0 for _ in range(V)]

	def findSet(self, x: int) -> int:
		if x != self.pi[x]:
			self.pi[x] = self.findSet(self.pi[x])
		return self.pi[x]

	def same(self, x: int, y: int) -> bool:
		return self.findSet(x) == self.findSet(y)

	def link(self, x: int, y: int) -> None:
		if self.rank[x] > self.rank[y]:
			self.pi[y] = x
		else:
			self.pi[x] = y
			if self.rank[x] == self.rank[y]:
				self.rank[y] += 1

	def unite(self, x: int, y: int) -> None:
		self.link(self.findSet(x), self.findSet(y))


class Edge:
	def __init__(self, source: int, target: int, cost: int) -> None:
		self.source = source
		self.target = target
		self.cost = cost


def kruskal(n: int, edges: List[Edge]) -> int:
	totalCost: int = 0
	edges.sort(key=lambda e: e.cost)
	uf: UnionFind = UnionFind(n + 1)
	for e in edges:
		if not uf.same(e.source, e.target):
			totalCost += e.cost
			uf.unite(e.source, e.target)
	return totalCost


if __name__ == "__main__":
	n, m = map(int, input().split())
	edges: List[Edge] = []
	for _ in range(m):
		s, t, c = map(int, input().split())
		edges.append(Edge(s, t, c))
	ans = kruskal(n, edges)
	print(ans)
