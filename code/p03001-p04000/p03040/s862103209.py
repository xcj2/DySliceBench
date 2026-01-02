import sys
import time
import heapq

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


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
    import bisect
    q = int(input())
    left = PriorityQueue([-INF], desc=True)
    right = PriorityQueue([INF])
    const = 0
    cur_f = 0
    length = 0

    for _ in range(q):
        val = list(map(int, readline().split()))
        if val[0] == 1:
            length += 1
            new_a = val[1]
            const += val[2]
            l = left.top()
            r = right.top()
            cur_x = l
            if length % 2 == 1:
                if new_a < l:
                    right.push(left.top())
                    left.push(new_a)
                    cur_f += abs(l - new_a)
                elif new_a <= r:
                    left.push(new_a)
                    right.push(new_a)
                else:
                    left.push(right.top())
                    right.push(new_a)
                    cur_f += abs(r - new_a)
            else:
                if new_a < l:
                    left.pop()
                    left.push(new_a)
                    cur_f += abs(l - new_a)
                else:
                    right.pop()
                    right.push(new_a)
                    cur_f += abs(r - new_a)
        else:
            print(left.top(), cur_f + const)


if __name__ == '__main__':
    main()
