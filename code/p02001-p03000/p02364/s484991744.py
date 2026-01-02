import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
G = []
E = []

class UnionFind:
	def __init__(self, n):
		self.rank = [0] * n
		self.parent = [0] * n
		self.make(n)

	def make(self, n):
		for i in range(n):
			self.parent[i] = i

	def unite(self, x, y):
		xroot = self.findset(x)
		yroot = self.findset(y)
		if self.rank[xroot] < self.rank[yroot]:
			self.parent[xroot] = yroot
		elif self.rank[xroot] > self.rank[yroot]:
			self.parent[yroot] = xroot
		else:
			self.parent[xroot] = yroot
			self.rank[yroot] += 1
			node = y
			while True:
				self.rank[node] += 1
				if self.parent[node] == node:
					break
				node = self.parent[node]
			self.rank[y] += 1

	def findset(self, x):
		if self.parent[x] == x:
			return x
		else:
			root = self.findset(self.parent[x])
			self.parent[x] = root
			return root

class Edge:
    def __init__(self, fr, to, w):
        self.fr = fr
        self.to = to
        self.w = w

def kruskal(v, e):
    global E
    E.sort(key=lambda x: x.w)
    uf = UnionFind(v)
    mst = []
    for i in range(e):
        if uf.findset(E[i].fr) != uf.findset(E[i].to):
            uf.unite(E[i].fr, E[i].to)
            mst.append(E[i])
    return mst


def main():
    global G, E
    n, e = map(int, input().strip().split())
    G = [[] for _ in range(n)]
    E = [0] * e
    for i in range(e):
        s, t, w = map(int, input().strip().split())
        E[i] = Edge(s, t, w)
    mst = kruskal(n, e)
    # print(mst)
    # from functools import reduce
    # print(reduce(lambda x, y: x.w + y.w, mst))
    ans = 0
    for q in mst:
        ans += q.w

    print(ans)

if __name__ == '__main__':
    main()

