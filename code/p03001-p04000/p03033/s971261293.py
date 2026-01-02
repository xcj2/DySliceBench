import sys
sys.setrecursionlimit(300000)
from bisect import bisect_left

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


# 区間updateと要素クエリ
class SegmentTree(object):

    def __init__(self, n, ele, segfun):
        self.ide_ele = ele
        self.segfun = segfun
        self.n = n
        self.N0 = 1 << n.bit_length()
        self.data = [self.ide_ele] * (self.N0 * 2)

    def update(self, l, r, val):
        l += self.N0
        r += self.N0
        while l < r:
            if l & 1:
                self.data[l] = self.segfun(self.data[l], val)
                l += 1
            if r & 1:
                self.data[r - 1] = self.segfun(self.data[r - 1], val)
                r -= 1
            l //= 2
            r //= 2

    def query(self, i):
        i += len(self.data) // 2
        ret = self.data[i]
        while i > 0:
            i //= 2
            ret = self.segfun(ret, self.data[i])
        return ret

N, Q = MI()
STX = [tuple(MI()) for _ in range(N)]
D = [I() for _ in range(Q)]

seg = SegmentTree(Q, INF, min)
for S, T, X in STX:
    # [S - X, T - X) に出発する人(l番目の人からr番目の人まで)が影響を受ける
    l = bisect_left(D, S - X)
    r = bisect_left(D, T - X)
    seg.update(l, r, X)

for i in range(Q):
    ans = seg.query(i)
    if ans == INF:
        print(-1)
    else:
        print(ans)