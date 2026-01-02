#!/usr/bin/env python3
import sys
import collections as cl


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()
    graph = [[] for i in range(N)]
    prev = [-1 for i in range(N)]
    colors = {}
    edges = []
    for _ in range(N-1):
        a, b = MI()
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
        edges.append([a-1, b-1])
    max_edge = 0
    max_edge_idx = -1
    for i in range(len(graph)):
        length = len(graph[i])
        if length >= max_edge:
            max_edge = length
            max_edge_idx = i

    deque = cl.deque([max_edge_idx])
    while len(deque) > 0:
        target = deque.popleft()
        pre = prev[target]
        pre_key = (target, pre) if target < pre else (pre, target)
        used_color = 0
        if pre != -1:
            used_color = colors[pre_key]

        connecteds = graph[target]
        color = 1
        for connected in connecteds:
            key = (target, connected) if target < connected else (
                connected, target)
            if key in colors:
                continue
            if color == used_color:
                color += 1
            colors[key] = color
            prev[connected] = target
            deque.append(connected)
            color += 1

    print(max_edge)

    for edge in edges:
        print(colors[(edge[0], edge[1])])


main()
