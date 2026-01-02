import sys
import bisect
readline = sys.stdin.readline
n = int(readline())
EP = []
l = -1000000001
u = 1000000001
vs_x = set()
h_num = 0
for _ in [0] * n:
    x1, y1, x2, y2 = (map(int, readline().split()))
    if x1 == x2:
        if y1 < y2:
            EP.append((y1, l, x1))
            EP.append((y2, u, x1))
        else:
            EP.append((y1, u, x1))
            EP.append((y2, l, x1))
        vs_x.add(x1)
    else:
        if x1 < x2:
            EP.append((y1, x1, x2))
        else:
            EP.append((y1, x2, x1))
        h_num += 1
class BinaryIndexedTree:
    __slots__ = ('data', 'num')
    def __init__(self, n):
        self.data = [0] * (n + 1)
        self.num = n
    def switch(self, i, d):
        while i <= self.num:
            self.data[i] += d
            i += i & -i
    def _sum(self, i):
        s = 0
        while i:
            s += self.data[i]
            i -= i & -i
        return s
    def seg_sum(self, a, b):
        return self._sum(b) - self._sum(a - 1)
EP.sort()
BIT = BinaryIndexedTree(len(vs_x))
vs_x = [l] + sorted(vs_x)
d_vs_x = {e: i for i, e in enumerate(vs_x)}
cnt = 0
for p in EP:
    e = p[1]
    if e == l:
        BIT.switch(d_vs_x[p[2]], 1)
    elif e == u:
        BIT.switch(d_vs_x[p[2]], -1)
    else:
        l_x = bisect.bisect_left(vs_x, e)
        r_x = bisect.bisect(vs_x, p[2]) - 1
        cnt += BIT.seg_sum(l_x, r_x)
        h_num -= 1
    if h_num == 0: break
print(cnt)