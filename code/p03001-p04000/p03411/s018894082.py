#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict

INF = float("inf")

def getlist():
	return list(map(int, input().split()))

# Dinic's algorithm
from collections import deque
class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

#無向グラフ？
#    def add_multi_edge(self, v1, v2, cap1, cap2):
#        edge1 = [v2, cap1, None]
#        edge1[2] = edge2 = [v1, cap2, edge1]
#        self.G[v1].append(edge1)
#        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

#処理内容
def main():
	N = int(input())
	A = []
	B = []
	for i in range(N):
		a, b = getlist()
		A.append([a, b])
	for i in range(N):
		c, d = getlist()
		B.append([c, d])

	G = Dinic(2 * N + 2)
	for i in range(N):
		G.add_edge(0, i + 1, 1)
		G.add_edge(N + 1 + i, 2 * N + 1, 1)
	for i in range(N):
		for j in range(N):
			if A[i][0] < B[j][0] and A[i][1] < B[j][1]:
				G.add_edge(i + 1, N + 1 + j, 1)
	print(G.flow(0, 2 * N + 1))


if __name__ == '__main__':
	main()