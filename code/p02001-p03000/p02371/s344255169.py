from typing import List, Deque
from collections import deque

INF = 1 << 89

# 重み付き枝（隣接リストで表現）
class Edge:
	def __init__(self, t: int, w: int) -> None:
		self.t = t # to vertex t
		self.w = w # weight w

# Treeに対してbfs（閉路を気にしなくてよい）
def bfs(s: int) -> List[int]:
	d: List[int] = [INF for _ in range(n)]
	Q: Deque[int] = deque()
	Q.append(s)
	d[s] = 0
	while len(Q) > 0:
		u = Q.popleft()
		for e in G[u]:
			if d[e.t] == INF:
				d[e.t] = d[u] + e.w
				Q.append(e.t)
	return d

def solve() -> int:
	d: List[int] = bfs(0)
	maxv: int = 0
	tgt: int = 0
	for i in range(n):
		if d[i] == INF:
			continue
		if maxv < d[i]:
			maxv = d[i]
			tgt = i
	d = bfs(tgt)
	maxv = 0
	for i in range(n):
		if d[i] == INF:
			continue
		maxv = max(maxv, d[i])
	return maxv

if __name__ == "__main__":
	n = int(input())
	G: List[Edge] = [[] for _ in range(n)]
	for _ in range(n - 1): # 木の枝数は（節点数 - 1）
		s, t, w = map(int, input().split())
		G[s].append(Edge(t, w))
		G[t].append(Edge(s, w))
	ans = solve()
	print(ans)
