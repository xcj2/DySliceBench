import sys
sys.setrecursionlimit(10 ** 8)


def lowLink(N: int, Adj: list):
	articulation = []
	bridge = []
	order = [None] * N
	lowest = [1 << 100] * N

	def _dfs(cur, pre, k):
		order[cur] = lowest[cur] = k
		is_articulation = False
		cnt = 0
		for nxt in Adj[cur]:
			if order[nxt] is None:
				cnt += 1
				_dfs(nxt, cur, k + 1)
				if lowest[cur] > lowest[nxt]:
					lowest[cur] = lowest[nxt]
				is_articulation |= pre >= 0 and lowest[nxt] >= order[cur]
				if order[cur] < lowest[nxt]:
					bridge.append((cur, nxt))
			elif nxt != pre and lowest[cur] > order[nxt]:
				lowest[cur] = order[nxt]
		is_articulation |= pre < 0 and cnt > 1
		if is_articulation:
			articulation.append(cur)

	_dfs(0, -1, 0)
	return articulation, bridge


def main():
	n, m, *L = map(int, open(0).read().split())
	adj = [[] for _ in range(n)]
	for s, t in zip(*[iter(L)] * 2):
		adj[s] += t,
		adj[t] += s,
	articulation, _ = lowLink(n, adj)
	if articulation:
		print("\n".join(map(str, sorted(articulation))))


if __name__ == '__main__':
	main()

