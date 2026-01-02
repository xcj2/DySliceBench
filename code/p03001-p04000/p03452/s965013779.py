import sys
sys.setrecursionlimit(100000)
N, M = map(int, input().split())
union = list(range(N + 1))
dist = [0] * (N + 1)
rec = [0] * (N + 1)

def ascend(anc):
	count = 0
	while anc != union[anc]:
		rec[count] = anc
		anc = union[anc]
		count += 1
	rec[count] = anc
	for i in range(count - 1, -1, -1):
		dist[rec[i]] += dist[rec[i + 1]]
		union[rec[i]] = anc
	return anc

def connect(l, r, d):
	l_anc = ascend(l)
	r_anc = ascend(r)
	if l_anc != r_anc:
		union[l_anc] = r_anc
		dist[l_anc] = dist[r] + d - dist[l]

def is_union(l, r):
	return ascend(l) == ascend(r)

def check(l, r, d):
	return dist[r] + d == dist[l]

for i in range(M):
	l, r, d = map(int, input().split())
	if is_union(l, r):
		if not check(l, r, d):
			print("No")
			break
	else:
		connect(l, r, d)
else:
	print("Yes")
