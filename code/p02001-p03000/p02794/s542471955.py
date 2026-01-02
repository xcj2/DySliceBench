import sys
def input():
	return sys.stdin.readline()[:-1]

n = int(input())
adj = [[] for _ in range(n)]
for i in range(n-1):
	a, b = map(int, input().split())
	adj[a-1].append((b-1, i))
	adj[b-1].append((a-1, i))
paths = [[0 for _ in range(n)] for _ in range(n)]

def pop_count(b):
	return sum(map(int, list(bin(b)[2:])))

def dfs(x, p, bit):
	for v, j in adj[x]:
		if v == p or paths[p][v] > 0:
			continue
		paths[p][v] = bit + (1<<j)
		dfs(v, p, bit + (1<<j))
	return

for i in range(n):
	dfs(i, i, 0)

#print(*paths, sep="\n")

cons = []
m = int(input())
for _ in range(m):
	u, v = map(int, input().split())
	cons.append(paths[u-1][v-1])

#print(cons)

uses = [0 for _ in range(1<<m)]
ans = 1<<(n-1)
for b in range(1, 1<<m):
	pop = pop_count(b) % 2
	cur = 0
	while not (1<<cur) & b:
		cur += 1
	use = uses[b - (1<<cur)] | cons[cur]
	uses[b] = use
	if pop:
		ans -= 1 << (n-1 - pop_count(use))
	else:
		ans += 1 << (n-1 - pop_count(use))

print(ans)