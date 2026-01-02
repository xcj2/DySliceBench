import sys
def input():
	return sys.stdin.readline()[:-1]

n, m = map(int, input().split())
def calc(x, y):
	return x * (x-1) // 2 + y * (y-1) // 2

adj = [[True for _ in range(n)] for _ in range(n)]
for _ in range(m):
	a, b = map(int, input().split())
	adj[a-1][b-1] = False
	adj[b-1][a-1] = False
for i in range(n):
	adj[i][i] = False

parity = [-1 for _ in range(n)]
nibus = []

def dfs(x):
	global bip
	bip[parity[x]] += 1
	for i in range(n):
		if adj[x][i] == True:
			if parity[i] < 0:
				parity[i] = 1^parity[x]
				dfs(i)
			elif parity[i] == parity[x]:
				print(-1)
				sys.exit()
	return bip

for i in range(n):
	if parity[i] < 0:
		parity[i] = 0
		bip = [0, 0]
		nibus.append(dfs(i))

cand = {0}
for p, q in nibus:
	p_set, q_set = set(), set()
	for s in cand:
		p_set.add(s+p)
		q_set.add(s+q)
	cand = p_set|q_set

ans = n**2
for c in cand:
	ans = min(ans, calc(c, n-c))
print(ans)