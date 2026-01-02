
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
					if cur < nxt:
						bridge.append((cur, nxt))
					else:
						bridge.append((nxt, cur))
			elif nxt != pre and lowest[cur] > order[nxt]:
				lowest[cur] = order[nxt]
		is_articulation |= pre < 0 and cnt > 1
		if is_articulation:
			articulation.append(cur)

	"""
	kk = 0
	for i in range(N):
		if order[i] is None:
			kk = _dfs(i, -1, kk)
	"""
	_dfs(0, -1, 0)
	return articulation, bridge

def main():
	n,m,*L=map(int,open(0).read().split())
	con=[[] for _ in range(n)]
	for a,b in zip(*[iter(L)]*2):
		con[a-1].append(b-1)
		con[b-1].append(a-1)
	_,br=lowLink(n,con)
	print(len(br))

if __name__ == '__main__':
	main()