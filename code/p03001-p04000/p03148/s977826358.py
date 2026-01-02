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
    from operator import itemgetter

    n, k = list(map(int, readline().split()))
    sushis_original = [list(map(int, readline().split())) for _ in range(n)]

    sushis_original.sort(key=itemgetter(1))
    sushis_original.sort(key=itemgetter(0))

    new_type = 0
    prev = -1
    for i in range(n):
        cur = sushis_original[i][0]
        if prev != cur:
            new_type += 1
        if cur > new_type:
            sushis_original[i][0] = new_type
        prev = cur

    type_num = sushis_original[-1][0]

    sushis = {i: [] for i in range(1, type_num + 1)}

    for sushi_type, val in sushis_original:
        sushis[sushi_type].append(val)

    eat_sushis = PriorityQueue()
    rem_sushis = PriorityQueue(desc=True)
    rem = k

    if rem >= type_num:
        for i in range(1, type_num + 1):
            eat_sushis.push(sushis[i].pop())
        rem -= type_num
        for vals in sushis.values():
            for val in vals:
                rem_sushis.push(val)
        for _ in range(rem):
            eat_sushis.push(rem_sushis.pop())
    else:
        for i in range(1, type_num + 1):
            eat_sushis.push(sushis[i].pop())
        discard_num = type_num - k
        for _ in range(discard_num):
            eat_sushis.pop()
        for vals in sushis.values():
            for val in vals:
                rem_sushis.push(val)

    cur_type = min(k, type_num)
    sub_next = 2 * cur_type - 1

    while rem_sushis:
        cur_val = eat_sushis.top()
        new_val = rem_sushis.top()
        diff = new_val - cur_val
        if diff >= sub_next:
            eat_sushis.pop()
            eat_sushis.push(rem_sushis.pop())
            cur_type -= 1
            sub_next = 2 * cur_type - 1
        else:
            break

    ans = cur_type ** 2 + eat_sushis.sum()

    print(ans)


if __name__ == '__main__':
    main()
