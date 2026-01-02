import sys
import collections
input = sys.stdin.readline

N, M, K = map(int, input().split())
F = []
for i in range(M):
	F.append(list(map(int, input().split())))
B = []
for i in range(K):
	B.append(list(map(int, input().split())))

def get_group(F):
	def root(a):
		p = G[a]
		while p != G[p]:
			p = G[p]
		while a != p:
			a, G[a] = G[a], p
		return p
	def union(a, b):
		ra = root(a)
		rb = root(b)
		if ra == rb: return
		G[ra] = rb
	G = [i for i in range(N)]
	for a, b in F:
		a -= 1
		b -= 1
		union(a, b)
	for i in range(N):
		G[i] = root(i)
	return G

def calc_count(F, G):
	edges = collections.defaultdict(set)
	for a, b in F:
		a -= 1
		b -= 1
		if G[a] == G[b]:
			edges[a].add(b)
			edges[b].add(a)
	cnt = [0] * N
	for i in range(N):
		cnt[i] = len(edges[i])
	return cnt

def get_num(c, f, b):
	ret = (c-1) - f - b
	return ret

G = get_group(F)
C = collections.Counter(G)
FC = calc_count(F, G)
BC = calc_count(B, G)
ans = [0] * N
for i in range(N):
	ans[i] = get_num(C[G[i]], FC[i], BC[i])

print(' '.join(map(str, ans)))
