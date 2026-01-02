#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    n, q = MI()
    connected_graph = [[] for i in range(n)]
    for i in range(n - 1):
        a, b = MI()
        connected_graph[b - 1].append(a - 1)
        connected_graph[a - 1].append(b - 1)

    points = [0] * n

    for j in range(q):
        p, x = MI()
        points[p - 1] += x

    ans = [-1] * n
    ans[0] = points[0]
    queue = cl.deque([])
    queue.append(0)
    while len(queue) > 0:
        target = queue.popleft()
        connecteds = connected_graph[target]
        for connected in connecteds:
            if ans[connected] != -1:
                continue
            else:
                ans[connected] = ans[target] + points[connected]
                queue.append(connected)

    print(*ans, sep=" ")


main()
