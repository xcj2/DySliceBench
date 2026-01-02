from sys import stdin
from collections import deque

def read_graph(n):
    A = [ [0]*(n+1) for _ in range(n+1) ]
    for _ in range(n):
        line = deque(stdin.readline().strip().split())
        i = line.popleft()
        line.popleft()
        for k in line:
            A[int(i)][int(k)] = 1
    return A

def bfs_ctrl(n, A):
    color = ["WHITE"] * (n+1)
    d = [-1] * (n+1)
    Q = deque([])

    def bfs(s):
        nonlocal color
        nonlocal d
        nonlocal Q
        color[s] = "GRAY"
        d[s] = 0
        Q.append(s)

        while Q:
            u = Q.popleft()
            for v in range(1, n+1):
                if A[u][v] and color[v] == "WHITE":
                    color[v] = "GRAY"
                    d[v] = d[u] + 1
                    Q.append(v)

            color[u] = "BLACK"

    bfs(1)
    for i in range(1, n+1):
            print(i, d[i])

n = int(input())
A = read_graph(n)
bfs_ctrl(n, A)
