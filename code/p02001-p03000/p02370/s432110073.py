from sys import stdin
from collections import deque

def read_graph(n, k):
    A = [ [] for _ in range(n) ]
    for _ in range(k):
        line = stdin.readline().strip().split()
        A[int(line[0])].append(int(line[1]))
    return A

def topological_sort(n, A):
    color = ["WHITE"] * n
    Q = deque([])
    out = []

    indeg = [0] * n
    for i in range(n):
        for j in A[i]:
            indeg[j] = indeg[j] + 1

    def bfs(s):
        nonlocal color
        nonlocal indeg
        nonlocal Q
        color[s] = "GRAY"
        Q.append(s)

        while Q:
            u = Q.popleft()
            out.append(u)

            for v in A[u]:
                indeg[v] = indeg[v] - 1
                if indeg[v] == 0 and color[v] == "WHITE":
                    color[v] = "GRAY"
                    Q.append(v)

    for i in range(n):
        if indeg[i] == 0 and color[i] == "WHITE":
            bfs(i)

    return out

n, k = [int(i) for i in input().split()]
A = read_graph(n, k)
B = topological_sort(n, A)
for i in B:
    print(i)

