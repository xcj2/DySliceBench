import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')

# 要素updateと区間クエリ
class SegmentTree(object):

    def __init__(self, A, e, fn):  # O(N)
        """
        :param A: 区間クエリの対象となる配列
        :param e: 単位元 fn(a, e) = fn(e, a) = a
        :param fn: (a, b) -> x な関数 a, bは交換則を満たす
        """
        self.e = e
        self.fn = fn
        self.length = 2 ** (len(A) - 1).bit_length()
        self.tree = [e] * 2 * self.length
        for i in range(len(A)):
            self.tree[i + self.length - 1] = A[i]
        for i in reversed(range(self.length - 1)):
            self.tree[i] = self.fn(self.tree[2 * i + 1], self.tree[2 * i + 2])

    # 配列のi番目をxに更新する
    def update(self, i, x):  # O(logN)
        i += self.length - 1
        self.tree[i] = x
        while i:
            i = (i - 1) // 2
            self.tree[i] = self.fn(self.tree[i * 2 + 1], self.tree[i * 2 + 2])

    # 区間[p, q)に関するクエリに答える
    def query(self, p, q):  # O(logN)
        if q <= p:
            return self.e
        p += self.length - 1
        q += self.length - 2
        res = self.e
        while q - p > 1:
            if p & 1 == 0:
                res = self.fn(res, self.tree[p])
            if q & 1 == 1:
                res = self.fn(res, self.tree[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = self.fn(res, self.tree[p])
        else:
            res = self.fn(self.fn(res, self.tree[p]), self.tree[q])
        return res

    # 現在のi番目の要素を取得する
    def at(self, i):  # O(1)
        return self.tree[i + self.length - 1]


N, Q = MI()
C = LMI()
LR = []
for i in range(Q):
    l, r = MI0()
    LR.append((i, l, r))

LR.sort(key=lambda x: x[2])
seg = SegmentTree([0] * N, 0, lambda a, b: a + b)
idx = dict()
cur = 0
ans = [0] * Q
for i, l, r in LR:
    while cur <= r:
        if C[cur] in idx:
            seg.update(idx[C[cur]], 0)
            seg.update(cur, 1)
            idx[C[cur]] = cur
        else:
            seg.update(cur, 1)
            idx[C[cur]] = cur
        cur += 1
    ans[i] = seg.query(l, r + 1)
for a in ans:
    print(a)