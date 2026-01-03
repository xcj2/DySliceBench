# encoding:utf-8
import sys
 
def main():
	n = int(input())
	vers = [list(map(int, input().split())) for _ in range(n - 1)]
	q, k = list(map(int, input().split()))
	queries = [list(map(int, input().split())) for _ in range(q)]
 
	#n = 10 ** 5
	#vers = [[i + 1, i + 2, 10 ** 9] for i in range(n - 1)]
 
	new_vers = mapping(n, vers)
	dist = calcMinDist(n, new_vers, k, queries)
	calcQueries(dist, queries, k)
	
def mapping(n, vers):
	new_vers = {i :[] for i in range(n)}
	for ver in vers:
		new_vers[ver[0] - 1].append((ver[1], ver[2]))
		new_vers[ver[1] - 1].append((ver[0], ver[2]))
	return new_vers
 
def calcMinDist(n, new_vers, k, queries):
	dist = [- 1 for _ in range(n)]
	flag = [False for _ in range(n)]
	dist[k - 1] = 0
	flag[k - 1] = True
	dfs(new_vers, dist, flag, k)
	return dist
 
def dfs(new_vers, dist, flag, frm):
	flag[frm - 1] = True
	vs = new_vers[frm - 1]
	for v in vs:
		if flag[v[0] - 1] == False:
			dist[v[0] - 1] = dist[frm - 1] + v[1]
			new_ver, dist, flag, _ = dfs(new_vers, dist, flag, v[0])
 
	return [new_vers, dist, flag, frm]
 
def calcQuery(dist, query, k):
	print(dist[query[0] - 1] + dist[query[1] - 1])
 
def calcQueries(dist, queries, k):
	for query in queries:
		calcQuery(dist, query, k)
 
if __name__ == '__main__':
	sys.setrecursionlimit(1000000)
	main()