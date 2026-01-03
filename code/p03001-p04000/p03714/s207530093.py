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
    n = int(readline())
    a = list(map(int, readline().split()))

    first = a[:n]
    second = a[n:2 * n]
    third = a[2 * n:3 * n]

    first_max = [0] * (n + 1)
    third_min = [0] * (n + 1)

    first_max[0] = sum(first)
    third_min[0] = sum(third)

    pq_first = PriorityQueue(first)
    cur = first_max[0]
    for i, x in enumerate(second, 1):
        if pq_first.top() < x:
            cur -= pq_first.pop()
            cur += x
            pq_first.push(x)
        first_max[i] = cur

    pq_third = PriorityQueue(third, desc=True)
    cur = third_min[0]
    for i, x in enumerate(second[::-1], 1):
        if pq_third.top() > x:
            cur -= pq_third.pop()
            cur += x
            pq_third.push(x)
        third_min[i] = cur

    ans = -INF
    for i in range(n + 1):
        fi_idx = i
        th_idx = n - i
        ans = max(ans, first_max[fi_idx] - third_min[th_idx])

    print(ans)


if __name__ == '__main__':
    main()
