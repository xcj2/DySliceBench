import sys
from bisect import bisect_left, bisect

sys.setrecursionlimit(10 ** 5 + 5)


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
            self.table[r1] += d2
        else:
            self.table[r1] = r2
            self.table[r2] += d1


def solve(n, m, aaa, bbb, lll, rrr):
    aaa, bbb = map(list, zip(*sorted(zip(aaa, bbb))))
    b_diff = [bbb[0]] + [b0 ^ b1 for b0, b1 in zip(bbb, bbb[1:])] + [bbb[-1]]
    cords = [set() for _ in range(n + 1)]
    uft = UnionFind(n + 1)
    for i, (l, r) in enumerate(zip(lll, rrr), start=1):
        li = bisect_left(aaa, l)
        ri = bisect(aaa, r)
        if li == ri or uft.find(li, ri):
            continue
        cords[li].add((ri, i))
        cords[ri].add((li, i))
        uft.union(li, ri)

    use_cords = set()

    def dfs(v, p):
        res = b_diff[v]
        for u, cord in cords[v]:
            if u == p:
                continue
            ret = dfs(u, v)
            if ret == 1:
                use_cords.add(cord)
            b_diff[u] = 0
            res ^= ret
        return res

    for v in range(n + 1):
        if b_diff[v]:
            b_diff[v] = dfs(v, -1)

    if sum(b_diff) == 0:
        print(len(use_cords))
        print(*sorted(use_cords))
    else:
        print(-1)


inp = list(map(int, sys.stdin.buffer.read().split()))
n, m = inp[:2]
aaa = inp[2:2 * n + 2:2]
bbb = inp[3:2 * n + 2:2]
lll = inp[2 * n + 2::2]
rrr = inp[2 * n + 3::2]
solve(n, m, aaa, bbb, lll, rrr)
