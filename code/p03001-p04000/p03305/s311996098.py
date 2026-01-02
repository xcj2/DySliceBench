import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

import heapq
class Heapq:
    def __init__(self, que=[], asc=True):
        if not asc:
            que = [-a for a in que]
        self.__que = que
        heapq.heapify(self.__que)
        self.__sign = 1 if asc else -1

    def pop(self):
        return heapq.heappop(self.__que) * self.__sign

    def push(self, value):
        heapq.heappush(self.__que, value * self.__sign)

    def pushpop(self, value):
        return heapq.heappushpop(self.__que, value * self.__sign) * self.__sign

    def top(self):
        return self.__que[0] * self.__sign

    def size(self):
        return len(self.__que)

def sol():
    N, M, start, end = map(int, input().split())
    start -= 1
    end -= 1
    edgeA = [[] for _ in range(N)]
    edgeB = [[] for _ in range(N)]

    for _ in range(M):
        fr, to, a, b = map(int, input().split())
        fr -= 1
        to -= 1
        edgeA[fr].append((to, a))
        edgeA[to].append((fr, a))
        edgeB[fr].append((to, b))
        edgeB[to].append((fr, b))

    minDistA = [float('inf')] * N
    minDistB = [float('inf')] * N

    que = Heapq([])
    que.push((0, start))

    while que.size():
        dist, now = que.pop()

        if minDistA[now] <= dist:
            continue

        minDistA[now] = dist

        for to, cost in edgeA[now]:
            if minDistA[to] > dist + cost:
                que.push((cost + dist, to))

    que = Heapq([])
    que.push((0, end))

    while que.size():
        dist, now = que.pop()

        if minDistB[now] <= dist:
            continue

        minDistB[now] = dist

        for to, cost in edgeB[now]:
            if minDistB[to] > dist + cost:
                que.push((cost + dist, to))

    ans = [float('inf')] * (N + 1)
    for day in range(N)[:: -1]:
        newDist = minDistA[day] + minDistB[day]
        ans[day] = min(ans[day + 1], newDist)

    offset = 10**15
    for a in ans[: N]:
        print(offset - a)

sol()