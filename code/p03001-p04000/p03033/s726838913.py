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
    XST = [0]*N
    for i in range(N):
        s, t, x = map(int, input().split())
        XST[i] = (x, s-x, t-x)
    D = [0]*Q
    for i in range(Q):
        D[i] = int(input())
    event = []
    for x, s, t in XST:
        event.append((s, 1, x))
        event.append((t, -1, x))

    event.sort()

    head = 0
    stack = ErasableHeap()
    for t, p, x in event:
        while D[head] < t:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.front())
            head += 1
            if head >= Q:
                return
        if p == 1:
            stack.push(x)
        else:
            stack.erase(x)

    while head < len(D):
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.front())
        head += 1
        if head >= Q:
            return


if __name__ == '__main__':
    main()
