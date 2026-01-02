import sys
import io
#sys.stdin = io.StringIO(input_string)
sys.setrecursionlimit(10 ** 6)
def input():
    return sys.stdin.readline()[:-1]
    
def resolve():
	from collections import deque
	
	n, q = map(int, input().split())
	adj = [[] for i in range(n+1)]
	for i in range(n-1):
		a, b = map(int, input().split())
		adj[a-1].append(b-1)
		adj[b-1].append(a-1)
	ans = [0 for i in range(n)]
	for i in range(q):
		p, x = map(int, input().split())
		p -= 1
		ans[p] += x
#	print(f"{adj=}\n{ans=}")

	def dfs(now, prv):
		for next in adj[now]:
#			print(f"{now=}, {next=}")
			if next == prv:
				continue
			ans[next] += ans[now]
			dfs(next, now)

	dfs(0, 0)
	print(*ans)

resolve()
