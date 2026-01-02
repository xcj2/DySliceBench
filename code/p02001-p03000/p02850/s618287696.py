'''input
6
1 2
1 3
1 4
1 5
1 6
'''
# A coding delight
from sys import stdin, stdout
import gc
gc.disable()
input = stdin.readline
from collections import defaultdict
import sys, threading


def get_source(graph):
	for i in graph:
		return i


def make(first, second):
	return str(first) + ' ' + str(second)


def dfs(graph, node, visited, color, medges, mx_c):
	visited[node] = True
	c = 1
	for i in graph[node]:
		if i not in visited:
			if color[node] == c:
				c += 1
			color[i] = c
			medges[make(node, i)] = c
			medges[make(i, node)] = c
			mx_c[0] = max(mx_c[0], c)
			c += 1
			dfs(graph, i, visited, color, medges, mx_c)


# main starts
def main():
	graph = defaultdict(list)
	n = int(input().strip())
	edges = []
	for _ in range(n - 1):
		u, v = list(map(int, input().split()))
		graph[u].append(v)
		graph[v].append(u)
		edges.append([u, v])

	s = get_source(graph)
	color = dict()
	visited = dict()
	color[s] = 0
	medges = dict()
	mx_c =[0]
	dfs(graph, s, visited, color, medges, mx_c)

	print(mx_c[0])
	for i, j in edges:
		print(medges[make(i, j)])


if __name__ == '__main__':
	sys.setrecursionlimit(100005)
	threading.stack_size(1 << 27)
	thread = threading.Thread(target = main)
	thread.start()

