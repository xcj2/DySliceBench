import sys
sys.setrecursionlimit(10**6)
def input():
	return sys.stdin.readline()[:-1]

n = int(input())
a = list(map(int, input().split()))
adj = [[] for _ in range(n)]
for _ in range(n-1):
	s, t = map(int, input().split())
	adj[s-1].append(t-1)
	adj[t-1].append(s-1)
par = [-1 for _ in range(n)]
aff = [0 for _ in range(n)]

def dfs(x, p):
	for v in adj[x]:
		if v == p:
			continue
		aff[x] += 1
		par[v] = x
		dfs(v, x)
	return
dfs(0, -1)
af_lis = [[] for _ in range(n)]
zero = [i for i in range(n) if aff[i] == 0]

def check(x):
	if af_lis[x] == []:
		af_lis[par[x]].append(a[x])
		aff[par[x]] -= 1
		if aff[par[x]] == 0:
			zero.append(par[x])
		return
	s, ma = sum(af_lis[x]), max(af_lis[x])
	if ma*2 > s:
		s_mi = ma
	else:
		s_mi = (s+1)//2
	if s_mi <= a[x] <= s:
		if par[x] == -1:
			if len(af_lis[x]) > 1 and 2*a[x] != s:
				print("NO")
				sys.exit()
			elif len(af_lis[x]) == 1 and a[x] != s:
				print("NO")
				sys.exit()
			return
		af_lis[par[x]].append(2*a[x] - s)
		aff[par[x]] -= 1
		if aff[par[x]] == 0:
			zero.append(par[x])
		return
	else:
		print("NO")
		sys.exit()
		return

while zero:
	check(zero.pop())

print("YES")