# https://tjkendev.github.io/procon-library/python/string/rolling_hash.html
import sys
def input():
	return sys.stdin.readline()[:-1]

BASE, MOD = 80408696819889532, (1<<61)-1

class RollingHash():
	def __init__(self, s, base, mod):
		self.mod = mod
		self.pw = pw = [1]*(len(s)+1)

		l = len(s)
		self.h = h = [0]*(l+1)

		v = 0
		for i in range(l):
			# case of letters
			h[i+1] = v = (v * base + ord(s[i])) % mod
		v = 1
		for i in range(l):
			pw[i+1] = v = v * base % mod

	# [l. r)
	def get(self, l, r):
		return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod

	def concatenate(self, l1, r1, l2, r2):
		return (self.get(l1, r1) * self.pw[r2-l2] + self.get(l2, r2)) % self.mod

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
rh_s, rh_t = RollingHash(s_concat, BASE, MOD), RollingHash(t, BASE, MOD)
t_hash = rh_t.get(0, nt)

adj = [-1 for _ in range(ns)]
for i in range(ns):
	if rh_s.get(i, i+nt) == t_hash:
		if i == (i+nt)%ns:
			print(-1)
			sys.exit()
		adj[i] = (i+nt)%ns

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