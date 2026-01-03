import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

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
    N = int(input())
    edges = [[] for _ in range(N)]

    for _ in range(N - 1):
        fr, to, cost = map(int, input().split())
        fr -= 1
        to -= 1
        edges[fr].append((to, cost))
        edges[to].append((fr, cost))

    Q, K = map(int, input().split())
    K -= 1

    minDist = [float('inf')] * N
    que = Heapq([])
    que.push((0, K))

    while que.size():
        dist, now = que.pop()

        if minDist[now] < dist:
            continue
        minDist[now] = dist

        for to, cost in edges[now]:
            if minDist[to] > dist + cost:
                que.push((dist + cost, to))

    for _ in range(Q):
        fr, to = map(int, input().split())
        print(minDist[fr - 1] + minDist[to - 1])


sol()