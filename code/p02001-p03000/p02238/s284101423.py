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

def dfs_ctrl(n, A):
    color = ["WHITE"] * (n+1)
    d = [0] * (n+1)
    f = [0] * (n+1)
    time = 0

    def dfs(u):
        nonlocal color
        nonlocal time
        if color[u] == "WHITE":
            color[u] = "GRAY"
            time += 1
            d[u] = time

            for v in range(1, n+1):
                if A[u][v] and color[v] == "WHITE":
                    dfs(v)
            color[u] = "BLACK"
            time += 1
            f[u] = time

    for i in range(1, n+1):
        if color[i] == "WHITE":
            dfs(i)

    for i in range(1, n+1):
        print(i, d[i], f[i])

n = int(input())
A = read_graph(n)
dfs_ctrl(n, A)
