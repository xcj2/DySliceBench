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

    def __init__(self, A, e, fn):
        self.fn = fn
        self.length = 2 ** (len(A) - 1).bit_length()
        self.data = [e] * (self.length * 2)
        for i in range(len(A)):
            self.data[i + self.length - 1] = A[i]
        for i in reversed(range(self.length - 1)):
            self.data[i] = self.fn(self.data[2 * i + 1], self.data[2 * i + 2])

    # 区間[l, r)の値とxをfnで比較して更新する
    def update(self, l, r, x):  # O(logN)
        l += self.length
        r += self.length
        while l < r:
            if l & 1:
                self.data[l] = self.fn(self.data[l], x)
                l += 1
            if r & 1:
                self.data[r - 1] = self.fn(self.data[r - 1], x)
                r -= 1
            l //= 2
            r //= 2

    # i番目の要素の値を取得する
    def query(self, i):  # O(logN)
        i += len(self.data) // 2
        ret = self.data[i]
        while i > 0:
            i //= 2
            ret = self.fn(ret, self.data[i])
        return ret

N, Q = MI()
STX = [tuple(MI()) for _ in range(N)]
D = [I() for _ in range(Q)]

seg = SegmentTree([INF] * Q, INF, min)
for S, T, X in STX:
    # [S - X, T - X) に出発する人[l番目の人, r番目の人)が影響を受ける
    l = bisect_left(D, S - X)
    r = bisect_left(D, T - X)
    seg.update(l, r, X)

for i in range(Q):
    ans = seg.query(i)
    if ans == INF:
        print(-1)
    else:
        print(ans)