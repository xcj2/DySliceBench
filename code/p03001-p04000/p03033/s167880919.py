#!/usr/bin/env python3
import sys
from bisect import bisect_left, bisect_right
import heapq

INF = float("inf")


class ErasableHeap(object):
    # https://qiita.com/Salmonize/items/638da118cd621d2628d1
    def __init__(self):
        self.data = []
        self.event = []

    def push(self, x):
        return heapq.heappush(self.data, x)

    def erase(self, x):
        return heapq.heappush(self.event, x)

    def _check(self):
        while self.event and\
                self.data[0] == self.event[0]:
            heapq.heappop(self.data)
            heapq.heappop(self.event)

    def front(self):
        self._check()
        return self.data[0]

    def pop(self):
        self.check()
        return heapq.heappop(self.data)

    def __len__(self):
        self._check()
        return len(self.data)


def main():

    N, Q = map(int, input().split())
    event = []
    for i in range(N):
        s, t, x = map(int, input().split())
        event.append((s-x, 1, x))
        event.append((t-x, -1, x))
    # 番兵用のeventを追加しておく
    event.append((INF, +1, INF))
    event.sort()

    D = [0]*Q
    for i in range(Q):
        D[i] = int(input())

    head = 0
    stack = ErasableHeap()
    for t, p, x in event:
        while head < Q and D[head] < t:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.front())
            head += 1
        if p == 1:
            stack.push(x)
        else:
            stack.erase(x)


if __name__ == '__main__':
    main()
