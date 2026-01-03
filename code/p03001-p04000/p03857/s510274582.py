from collections import defaultdict as dd

N, K, L = list(map(int, input().split()))
PQ = [list(map(int, input().split())) for _ in range(K)]
RS = [list(map(int, input().split())) for _ in range(L)]

def uft_root(g, a):
	if g[a] < 0:
		return a
	g[a] = uft_root(g, g[a])
	return g[a]

def uft_size(g, a):
	return -g[uft_root(g, a)]

def uft_merge(g, a, b):
	a, b = uft_root(g, a), uft_root(g, b)
	if a == b:
		return
	size_a, size_b = uft_size(g, a), uft_size(g, b)
	if size_a < size_b:
		a, b = b, a
		size_a, size_b = size_b, size_a
	g[a] -= size_b
	g[b] = a

uft_pq = [-1] * N
uft_rs = [-1] * N

for p, q in PQ:
	p, q = p - 1, q - 1
	uft_merge(uft_pq, p, q)
for r, s in RS:
	r, s = r - 1, s - 1
	uft_merge(uft_rs, r, s)

group = dd(int)
for n in range(N):
	group[(uft_root(uft_pq, n), uft_root(uft_rs, n))] += 1

result = []
for n in range(N):
	result += [group[(uft_root(uft_pq, n), uft_root(uft_rs, n))]]
print(" ".join(map(str, result)))
