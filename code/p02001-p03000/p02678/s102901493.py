#!/usr/bin/env python3
import sys
from collections import deque


input = sys.stdin.readline
def IS(cb): return cb(input().strip())
def IL(cb): return [cb(s) for s in input().strip().split()]
def IR(cb, rows): return [IS(cb) for _ in range(rows)]
def ILL(cb, rows): return [IL(cb) for _ in range(rows)]


def solve():
    N, M = IL(int)
    AB = ILL(int, M)
    graph = [[] for _ in range(N)]
    for a, b in AB:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    que = deque()
    que.append(0)
    visited = [False] * N
    visited[0] = True
    route = [0] * N
    while len(que):
        current = que.popleft()
        for next in graph[current]:
            if not visited[next]:
                visited[next] = True
                que.append(next)
                route[next] = current + 1

    print('Yes')
    for i in route[1:]:
        print(i)


solve()
