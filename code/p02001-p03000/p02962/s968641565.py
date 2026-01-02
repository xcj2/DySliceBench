import sys
def input():
	return sys.stdin.readline()[:-1]

class KMP():
	def __init__(self, sentence):
		self.sentence = sent = sentence
		self.l = l = len(sent)
		self.table = table = [0 for _ in range(l+1)]
		table[0] = -1
		j = -1
		for i in range(l):
			while j >= 0 and sent[i] != sent[j]:
				j = table[j]
			j += 1
			if i < l-1 and sent[i+1] == sent[j]:
				table[i+1] = table[j]
			else:
				table[i+1] = j

	def search(self, key):
		table = self.table
		sent = self.sentence
		l = self.l
		i = 0
		res = []
		for j in range(len(key)):
			while i > -1 and sent[i] != key[j]:
				i = table[i]
			i += 1
			if i >= l:
				res.append(j-i+1)
				i = table[i]
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

adj = [-1 for _ in range(ns)]

kmp = KMP(t)
matches = kmp.search(s_concat)

for i in matches:
	if i >= ns:
		break
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