import sys
inp = sys.stdin.readline
read = lambda: list(map(int, inp().strip().split()))

sys.setrecursionlimit(10**6)
# def solve():
# 	n, m = read()
# 	graph = [[] for i in range(n+1)]
# 	for _ in range(m):
# 		u, v = read()
# 		graph[u].append(v)
# 	visited = [0 for i in range(n+1)]
# 	def dfs(node):
# 		if visited[node]:
# 			return(visited[node])
# 		if not graph[node]:
# 			visited[node] = 0
# 			return(0)
# 		m = 0
# 		for i in graph[node]:
# 			m = max(m, dfs(i))
# 		visited[node] = 1 + m#ax(dfs(i) for i in graph[node])
# 		# print(node, visited[node])
# 		return(visited[node])

# 	ans = 0
# 	for i in range(1, n+1):
# 		ans = max(ans, dfs(i))
# 	# print(visited)
# 	print(ans)


def grid():
	n, m = read()
	arr = []
	for i in range(n):
		arr.append(inp().strip())
	# dic = {}
	dp = [-1]*m*n
	# print(dp, len(dp))
	def count_paths(i, j):
		# key = str(i)+"-"+str(j)
		# if key in dic:
		# 	return(dic[key])
		key = (i*m + j)
		# print(key)
		if i == n-1 and j == m-1:
			dp[key] = 1
			return(1)
		if i == n or j == m:
			return(0)
		if arr[i][j] == "#":
			dp[key] = 0
			return(0)
		if dp[key] > -1:
			return(dp[key])
		paths = (count_paths(i+1, j) + count_paths(i, j+1)) % (10**9 + 7)
		# dic[key] = paths
		dp[key] = paths
		return(paths)
	print(count_paths(0, 0))

def grid2():
	n, m = read()
	arr = []
	for i in range(n):
		arr.append(inp().strip())
	dp = {}
	# print(dp, len(dp))
	def count_paths(i, j):
		key = str(i)+"-"+str(j)
		if key in dp:
			return(dp[key])
		# key = (i*m + j)
		# print(key)
		if key in dp:
			return(dp[key])
		if i == n-1 and j == m-1:
			dp[key] = 1
			return(1)
		if i == n or j == m:
			return(0)
		if arr[i][j] == "#":
			dp[key] = 0
			return(0)
		
		paths = (count_paths(i+1, j) + count_paths(i, j+1)) % (10**9 + 7)
		# dic[key] = paths
		dp[key] = paths
		return(paths)
	print(count_paths(0, 0))

def grid3():
	MOD = pow(10,9) + 7
	H, W = read()
	 
	grid = [[0]*W for h in range(H)]
	grid[0][0] = 1
	 
	for h in range(H) :  
	  row = input()
	 
	  for w in range(W) :
	    if row[w] == '#' : continue
	    if h > 0 : grid[h][w] += grid[h-1][w]
	    if w > 0 : grid[h][w] += grid[h][w-1]
	    grid[h][w] %= MOD
	print(grid[-1][-1]% MOD)


if __name__ == "__main__":
	# solve()
	grid3()