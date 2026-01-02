import sys
sys.setrecursionlimit(10**6)
def input():
	return sys.stdin.buffer.readline()[:-1]

MOD = 10**9 + 7
list_size = 200001

f_list = [1] * list_size
f_r_list = [1] * list_size

for i in range(list_size - 1):
	f_list[i + 1] = int((f_list[i] * (i + 2)) % MOD)

f_r_list[-1] = pow(f_list[-1], MOD - 2, MOD)

for i in range(2, list_size + 1):
	f_r_list[-i] = int((f_r_list[-i + 1] * (list_size + 2 - i)) % MOD)

def comb(n, r):
	if n < r:
		return 0
	elif n == 0 or r == 0 or n == r:
		return 1
	else:
		return (((f_list[n - 1] * f_r_list[n - r - 1]) % MOD) * f_r_list[r - 1]) % MOD 

n = int(input())
adj = [[] for _ in range(n)]
for _ in range(n-1):
	a, b = map(int, input().split())
	adj[a-1].append(b-1)
	adj[b-1].append(a-1)


dp_pat = [0 for _ in range(n)]
dp_num = [0 for _ in range(n)]


def dfs1(x, p):
	num = 0
	res = 1
	for v in adj[x]:
		if v == p:
			continue
		dfs1(v, x)
		num += dp_num[v]
		res *= comb(num, dp_num[v]) * dp_pat[v]
		res %= MOD
	dp_num[x] = num+1
	dp_pat[x] = res
	return

dfs1(0, -1)
ans = [0 for _ in range(n)]
ans[0] = dp_pat[0]

def dfs2(x, p):
	for v in adj[x]:
		if v == p:
			continue
		pres = [dp_pat[x], dp_num[x], dp_pat[v], dp_num[v]]
		dp_pat[x] *= pow(comb(dp_num[x]-1, dp_num[v]) * dp_pat[v], MOD-2, MOD)
		dp_pat[x] %= MOD
		dp_num[x] -= dp_num[v]

		dp_pat[v] *= comb(dp_num[x] + dp_num[v] - 1, dp_num[x]) * dp_pat[x]
		dp_pat[v] %= MOD
		dp_num[v] += dp_num[x]
		ans[v] = dp_pat[v]
		dfs2(v, x)
		dp_pat[x], dp_num[x], dp_pat[v], dp_num[v] = pres
	return

dfs2(0, -1)
print(*ans, sep="\n")