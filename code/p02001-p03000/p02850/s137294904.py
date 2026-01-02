import os
import sys
from collections import defaultdict
adj = defaultdict(list)
col = defaultdict(int)
sys.setrecursionlimit(1000000)
mx=0
edges = {}
def find_color(u , p):
	global mx , now
	cnt =0
	for i in adj[u]:
		cnt = cnt+1
		if i==p:
			continue
		find_color(i , u)
	mx = max(mx, cnt)
now =0
def dfs(u , p, prev):
	global mx, now
	for i in adj[u]:
		if i==p:
			continue
		if now == prev:
			now = (now+1)%mx
		col[edges[i,u]]=now
		now =(now+1)%mx
	for i in adj[u]:
		if i==p:
			continue
		dfs(i , u, col[edges[i, u]])

def main():
	n = int(input())
	for i in range(n-1):
		x, y = map(int , input().split())
		adj[x].append((y))
		adj[y].append((x))
		edges[x,y]=i
		edges[y,x]=i
	find_color(1, 0)
	dfs(1, 0,-1)
	print(mx)
	for i in range(n-1):
		print(col[i]+1)


if __name__ == "__main__":
	main()
