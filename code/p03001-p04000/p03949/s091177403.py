import sys
sys.setrecursionlimit(10**6)
INF = 10**7
def input():
	return sys.stdin.buffer.readline()[:-1]

n = int(input())
ver = [[-INF, INF] for _ in range(n)]
adj = [[] for _ in range(n)]
for i in range(n-1):
	a, b = map(int, input().split())
	adj[a-1].append(b-1)
	adj[b-1].append(a-1)

k = int(input())
for _ in range(k):
	w, p = map(int, input().split())
	ver[w-1] = [p, p]
	root = w-1

def dfs1(x, parent, bit):
	for v in adj[x]:
		if v == parent:
			continue
		else:
			if ver[v][1] != INF and ver[v][1]%2 == bit:
				print("No")
				sys.exit()
			dfs1(v, x, 1^bit)

dfs1(root, -1, ver[root][1]%2)

def dfs2(x, p):
	if p != -1 and len(adj[x]) == 1:
		return ver[x]
	else:
		for v in adj[x]:
			if v == p:
				continue
			else:
				m, M = dfs2(v, x)
				ver[x][0] = max(ver[x][0], m-1)
				ver[x][1] = min(ver[x][1], M+1)

		if ver[x][0] > ver[x][1]:
			print("No")
			sys.exit()
		else:
			return ver[x]

dfs2(root, -1)

ans = [INF for _ in range(n)]
ans[root] = ver[root][0]

def dfs3(x, p):
	for v in adj[x]:
		if v == p:
			continue
		else:
			if ver[v][0] <= ans[x]-1 <= ver[v][1]:
				ans[v] = ans[x] - 1
			else:
				ans[v] = ans[x] + 1
			dfs3(v, x)
	return

dfs3(root, -1)
print("Yes")
print(*ans, sep="\n")