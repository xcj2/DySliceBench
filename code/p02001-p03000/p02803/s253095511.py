from collections import deque
INF = 10 ** 9

class Edge:
	def __init__(self, t, w):
		self.t = t
		self.w = w

def around(i, j, H, W):
	if H == 1:
		if j == 0:
			ans = [(i, j+1)]
		elif j == W - 1:
			ans = [(i, j-1)]
		else:
			ans = [(i, j-1), (i, j+1)]
	elif W == 1:
		if i == 0:
			ans = [(i+1, j)]
		elif i == H - 1:
			ans = [(i-1, j)]
		else:
			ans = [(i-1, j), (i+1, j)]
	else:
		if i == 0:
			if j == 0:
				ans = [(i, j+1), (i+1, j)]
			elif j == W-1:
				ans = [(i, j-1), (i+1, j)]
			else:
				ans = [(i, j-1), (i, j+1), (i+1, j)]
		elif i == H - 1:
			if j == 0:
				ans = [(i-1, j), (i, j+1)]
			elif j == W-1:
				ans = [(i-1, j), (i, j-1)]
			else:
				ans = [(i-1, j), (i, j-1), (i, j+1)]
		else:
			if j == 0:
				ans = [(i-1, j), (i, j+1), (i+1, j)]
			elif j == W-1:
				ans = [(i-1, j), (i, j-1), (i+1, j)]
			else:
				ans = [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]
	return ans

def bfs(s):
	d = [INF for _ in range(H*W)]
	Q = deque()
	Q.append(s)
	d[s] = 0
	while len(Q) > 0:
		u = Q.popleft()
		for e in G[u]:
			if d[e.t] == INF:
				d[e.t] = d[u] + e.w
				Q.append(e.t)
	return d

def solve(s):
	d = bfs(s)
	maxv = 0
	tgt = 0
	for i in range(W*H):
		if d[i] == INF:
			continue
		if maxv < d[i]:
			maxv = d[i]
			tgt = i
	d = bfs(tgt)
	maxv = 0
	for i in range(W*H):
		if d[i] == INF:
			continue
		maxv = max(maxv, d[i])
	return maxv

if __name__ == "__main__":
	H, W = map(int, input().split())
	S = [[0 for j in range(W)] for i in range(H)]
	# print(S)
	for i in range(H):
		s = input()
		for j in range(W):
			if s[j] == "#":
				S[i][j] = 1
	# print(S)
	G = [[] for _ in range(H*W)]
	for i in range(H):
		for j in range(W):
			if S[i][j] != 1:
				for (k, l) in around(i, j, H, W):
					if S[k][l] != 1:
						G[i*W + j].append(Edge(k*W + l, 1))
						G[k*W + l].append(Edge(i*W + j, 1))

	ans = 0
	for i in range(H):
		for j in range(W):
			if S[i][j] != 1:
				v = solve(i*W + j)
				ans = max(ans, v)
	print(ans)