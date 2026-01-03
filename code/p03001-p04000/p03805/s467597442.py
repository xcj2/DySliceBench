# coding:utf-8

import sys
from collections import defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


n, m = LI()
graph = defaultdict(list)
for _ in range(m):
    a, b = LI_()
    graph[a].append(b)
    graph[b].append(a)


def DFS(v: int, visited: list) -> int:
    # print(visited, id(visited))
    ans = 0
    visited[v] = 1
    if all(visited):
        return 1

    for next in graph[v]:
        if visited[next]:
            continue

        ans += DFS(next, visited[:])

    return ans


print(DFS(0, [0] * n))
