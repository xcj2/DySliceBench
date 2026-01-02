import sys
input = sys.stdin.readline
from operator import add, itemgetter


class RMQ():
    
    def __init__(self, size, op=min, init_value=10**8):
        """初期化"""
        self.size = size
        self.op = op
        self.init_value = init_value
        n = 2 ** ((size-1).bit_length())
        treesize = n * 2
        st = [init_value] * treesize
        self.st = st
        self.offset = len(st) // 2

    @classmethod
    def from_array(cls, a, op=min, init_value=10**8):
        st = cls(len(a), op=op, init_value=init_value)
        for i, x in enumerate(a):
            st.update(i, x)
        return st

    def update(self, key, value):
        """値の更新"""
        k = self.offset + key
        self.st[k] = value
        k >>= 1
        while k > 0:
            self.st[k] = self.op(self.st[k * 2], self.st[k * 2 + 1])
            k >>= 1

    def _query_bottomup(self, a, b):
        """区間[a, b) に対する累積操作
        """
        a += self.offset
        b += self.offset - 1
        s = self.init_value
        while a < b:
            if a & 1:
                s = self.op(s, self.st[a])
                a += 1
            a >>= 1
            if not b & 1:
                s = self.op(s, self.st[b])
                b -= 1
            b >>= 1
        if a == b:
            s = self.op(s, self.st[a])
        return s

    def _query_topdown(self, a, b, k=1, l=0, r=-1):
        """区間[a, b) に対する累積操作
        k: 着目しているノード (1-indexed)
        l: 探索区間 st[l, r) の左端 (0-indexed)
        r: 探索区間 st[l, r) の右端 (0-indexed)
        """
        if r == -1:
            r = self.offset
        if r <= a or b <= l:
            return self.init_value
        if a <= l and r <= b:
            return self.st[k]
        mid = (l + r) // 2
        lv = self._query_topdown(a, b, k * 2, l, mid)
        rv = self._query_topdown(a, b, k * 2 + 1, mid, r)
        return self.op(lv, rv)

    def query(self, a, b):
        """区間[a, b) に対する累積操作"""
        if a > b:
            raise ValueError("a must be less than equal b.")
        return self._query_bottomup(a, b)


def read():
    N, Q = map(int, input().strip().split())
    C = list(map(int, input().strip().split()))
    # クエリ [l, r) とその順序を持っておく
    LRI = []
    for i in range(Q):
        l, r = map(int, input().strip().split())
        LRI.append((l-1, r, i))
    return N, Q, C, LRI


def solve(N, Q, C, LRI, INF=10**7):
    prev = [-1 for i in range(N+1)]
    ans = [0 for i in range(Q)]
    
    rmq = RMQ(N, op=add, init_value=0)
    # Rの昇順にソート
    LRI.sort(key=itemgetter(1))
    r_prev = 0
    for l, r, i in LRI:
        for j in range(r_prev, r):
            c = C[j]
            # A[prev[c]] = 0
            if prev[c] != -1:
                rmq.update(prev[c], 0)
            prev[c] = j
            # A[j] = 1
            rmq.update(j, 1)
        r_prev = r
        ans[i] = rmq.query(l, r)

    for a in ans:
        print(a)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
