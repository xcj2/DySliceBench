import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)

import heapq


class PriorityQueue:
    class Reverse:
        def __init__(self, val):
            self.val = val

        def __lt__(self, other):
            return self.val > other.val

        def __repr__(self):
            return repr(self.val)

    def __init__(self, x=None, desc=False):
        if not x:
            x = []
        if desc:
            for i in range(len(x)):
                x[i] = self.Reverse(x[i])
        self._desc = desc
        self._container = x
        heapq.heapify(self._container)

    @property
    def is_empty(self):
        return not self._container

    def pop(self):
        if self._desc:
            return heapq.heappop(self._container).val
        else:
            return heapq.heappop(self._container)

    def push(self, item):
        if self._desc:
            heapq.heappush(self._container, self.Reverse(item))
        else:
            heapq.heappush(self._container, item)

    def top(self):
        if self._desc:
            return self._container[0].val
        else:
            return self._container[0]

    def sum(self):
        return sum(self._container)

    def __len__(self):
        return len(self._container)


def main():
    from collections import deque, defaultdict
    N, M = map(int, readline().split())

    edge = defaultdict(list)

    for _ in range(M):
        l, r, c = map(int, readline().split())
        edge[l].append((r, c))
        edge[r].append((l, c))

    for i in range(1, N):
        edge[i + 1].append((i, 0))

    pq = PriorityQueue()
    pq.push((0, 1))
    dist = defaultdict(lambda: INF)

    while pq:
        cur, u = pq.pop()
        for v, c in edge[u]:
            nc = cur + c
            if nc < dist[v]:
                dist[v] = nc
                pq.push((nc, v))

    if dist[N] != INF:
        print(dist[N])
    else:
        print(-1)


if __name__ == '__main__':
    main()
