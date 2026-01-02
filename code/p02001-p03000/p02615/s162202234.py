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
            return self.val[0] > other.val[0]

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
    def f(p, q):
        ret = (min(p, q), max(p, q))
        return ret

    n = int(readline())
    a = list(map(int, readline().split()))
    a.sort(reverse=True)
    ans = a[0]
    pq = PriorityQueue(desc=True)
    pq.push(f(a[0], a[1]))
    pq.push(f(a[0], a[1]))

    for x in a[2:]:
        first, second = pq.pop()
        ans += first
        pq.push(f(first, x))
        pq.push(f(second, x))

    print(ans)


if __name__ == '__main__':
    main()
