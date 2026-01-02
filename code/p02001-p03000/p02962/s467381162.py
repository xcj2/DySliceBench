import sys
def input():
	return sys.stdin.readline()[:-1]

def Z_algorithm(s):
	l = len(s)
	res = [-1 for _ in range(l)]
	res[0] = l
	i, j = 1, 0
	while i < l:
		while i+j < l and s[j] == s[i+j]:
			j += 1
		res[i] = j

		if j == 0:
			i += 1
			continue
		else:
			k = 1
			while i+k < l and k + res[k] < j:
				res[i+k] = res[k]
				k += 1

			i += k
			j -= k

	return res

s = input()
s_concat = s
t = input()
ns, nt = len(s), len(t)

if ns == 1:
	if {s} == set(list(t)):
		print(-1)
	else:
		print(0)
	sys.exit()

while len(s_concat) < ns + nt - 1:
	s_concat += s
ts_concat = t + " " + s_concat
z = Z_algorithm(ts_concat)

adj = [-1 for _ in range(ns)]

for i in range(1, len(z)):
	if i-nt-1 >= ns:
		break
	if z[i] == nt:
		j = i-nt-1
		if j == (j+nt)%ns:
			print(-1)
			sys.exit()
		adj[j] = (j+nt)%ns

visited = [False for _ in range(ns)]
path_len = [0 for _ in range(ns)]

def dfs(x):
	cur = x
	res = 0
	while adj[cur] >= 0:
		visited[cur] = True
		if adj[cur] == x:
			print(-1)
			sys.exit()
		res += 1
		if path_len[adj[cur]] > 0:
			path_len[x] = path_len[adj[cur]] + res
			return path_len[adj[cur]] + res
		cur = adj[cur]
	path_len[x] = res
	return res

ans = 0
for i in range(ns):
	if not visited[i]:
		d = dfs(i)
		ans = max(ans, d)

if ans == ns:
	print(-1)
else:
	print(ans)