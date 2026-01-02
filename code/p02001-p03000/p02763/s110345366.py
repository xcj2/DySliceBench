import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


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
        for i in range(self.length - 2, -1, -1):
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


N = I()
S = input()
Q = [tuple(input().split()) for _ in range(I())]

A = [2 ** (ord(c) - 97) for c in S]
seg = SegmentTree(A, 0, lambda a, b: a | b)


for t, i, c in Q:
    if t == '1':
        i = int(i) - 1
        seg.update(i, 2 ** (ord(c) - 97))
    else:
        l, r = int(i) - 1, int(c)
        bit = seg.query(l, r)
        print(bin(bit).count('1'))
