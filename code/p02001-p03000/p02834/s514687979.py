import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque, Counter
def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
INF = 10 ** 20

def dfs(graph, root, n):
    dista = [INF for i in range(n)]
    visited = [0 for i in range(n)]
    dista[root - 1] = 0
    visited[root - 1] = 1
    d = deque()
    for edge in graph[root - 1]:
        d.append(edge)
    while(d):
        cur, nxt = d.pop()
        if not visited[nxt]:
            dista[nxt] = dista[cur] + 1
            visited[nxt] = 1
            for edge in graph[nxt]:
                d.append(edge)

    return dista

def dfs2(graph, root, n, dista):
    distb = [INF for i in range(n)]
    visited = [0 for i in range(n)]
    visited[root - 1] = 1
    distb[root-1] = 0
    d = deque()
    ans = dista[root-1]
    dec = 0
    # print(dista, distb)
    for edge in graph[root-1]:
        d.append(edge)
    while(d):
        # print(d)
        # print(distb)
        cur, nxt = d.pop()
        if not visited[nxt]:
            if distb[cur] + 1 <= dista[nxt]:
                if distb[cur] + 1 == dista[nxt]:
                    dec = 1
                visited[nxt] = 1
                distb[nxt] = distb[cur] + 1
                for edge in graph[nxt]:
                    d.append(edge)
                if ans < dista[nxt]:
                    ans = dista[nxt]

            # print(ans, cur, nxt, visited)

    return ans

def main():
    n, u, v = getList()
    graph = [[] for i in range(n)]
    dista = [INF for i in range(n)]
    distb = [INF for i in range(n)]
    for i in range(n-1):
        a,b = getList()
        graph[a-1].append((a-1, b-1))
        graph[b - 1].append((b-1, a - 1))
    # print(graph)
    if n == 3:
        print(1)
        return
    dista = dfs(graph, v, n)
    # print(dista)
    print(dfs2(graph, u, n, dista) - 1)
if __name__ == "__main__":
    main()

