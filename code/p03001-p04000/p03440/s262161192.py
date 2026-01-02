from collections import deque, defaultdict
from heapq import heapify, heappop, merge, heapreplace


class UnionFind:
    def __init__(self, n):
        self.table = [-1] * n

    def _root(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self._root(self.table[x])
            return self.table[x]

    def find(self, x, y):
        return self._root(x) == self._root(y)

    def union(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            if d1 == d2:
                self.table[r1] -= 1
        else:
            self.table[r1] = r2


def solve(aa, uft):
    roots = defaultdict(list)
    for x, a in enumerate(aa):
        roots[uft._root(x)].append(a)
    if len(roots) == 1:
        return 0
    if n < (len(roots) - 1) * 2:
        return 'Impossible'
    ans = 0
    queue = []
    for l in roots.values():
        l.sort()
        ans += l[0]
        queue.append(l[1:])
    lm = n - m - 2
    if lm > 0:
        mm = merge(*queue)
        for _ in range(lm):
            ans += next(mm)
    return ans


n, m = map(int, input().split())
aa = list(map(int, input().split()))
uft = UnionFind(n)
for _ in range(m):
    uft.union(*map(int, input().split()))
print(solve(aa, uft))
