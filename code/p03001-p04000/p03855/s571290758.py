from collections import defaultdict
def main():
	N, K, L = map(int, input().split())
	road = [0]*K
	rail = [0]*L
	road_graph = [[i, 0] for i in range(N+1)]
	rail_graph = [[i, 0] for i in range(N+1)]

	def root(graph, i):
		parent = graph[i][0]
		if parent == i:
			return i
		return root(graph, parent)

	def is_same_tree(graph, i, j):
		return root(graph, i) == root(graph, j)

	def unite(graph, i, j):
		if is_same_tree(graph, i, j):
			return
		l = graph[root(graph, i)]
		r = graph[root(graph, j)]
		if l[1] < r[1]:
			l[0] = r[0]
			r[1] += 1
		else:
			r[0] = l[0]
			l[1] += 1

	ans_list = [""]*N

	for i in range(K):
		road[i] = list(map(int, input().split()))
		unite(road_graph, road[i][0], road[i][1])
	for i in range(L):
		rail[i] = list(map(int, input().split()))
		unite(rail_graph, rail[i][0], rail[i][1])

	ans_memo = defaultdict(int)
	road_memo = [0]*(N+1)
	rail_memo = [0]*(N+1)
	for i in range(1, N+1):
		road_root = root(road_graph, i)
		rail_root = root(rail_graph, i)
		road_memo[i] = road_root
		rail_memo[i] = rail_root
		ans_memo[(road_root, rail_root)] += 1

	for i in range(1, N+1):
		road_root = road_memo[i]
		rail_root = rail_memo[i]
		this_ans = str(ans_memo[road_root, rail_root])
		ans_list[i-1] = this_ans

	ans = " ".join(ans_list)
	print(ans)


if __name__ == '__main__':
	main()