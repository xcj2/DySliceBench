import sys
input = sys.stdin.readline
from operator import or_


def read():
    N = int(input().strip())
    S = input().strip()
    Q = int(input().strip())
    return N, S, Q


class SegmentTree():
    
    def __init__(self, size, op=min, init_value=10**8):
        """初期化"""
        self.size = size
        self.op = op
        self.init_value = init_value
        n = 2 ** ((size-1).bit_length())
        treesize = n * 2
        st = [init_value for i in range(treesize)]
        self.st = st

    @classmethod
    def from_array(cls, a, op=min, init_value=10**8):
        st = cls(len(a), op=op, init_value=init_value)
        for i, x in enumerate(a):
            st.update(i, x)
        return st

    def update(self, key, value):
        """値の更新"""
        offset = len(self.st) // 2
        k = offset + key
        self.st[k] = value
        k >>= 1
        while k > 0:
            self.st[k] = self.op(self.st[k * 2], self.st[k * 2 + 1])
            k >>= 1

    def _query_bottomup(self, a, b):
        """区間[a, b) に対する累積操作
        """
        offset = len(self.st) // 2
        a += offset
        b += offset - 1
        s = self.init_value
        while a < b:
            if a & 1 == 1:
                s = self.op(s, self.st[a])
                a += 1
            a >>= 1
            if b & 1 == 0:
                s = self.op(s, self.st[b])
                b -= 1
            b >>= 1
        if a == b:
            s = self.op(s, self.st[a])
        return s

    def _query_topdown(self, a, b, k, l, r):
        """区間[a, b) に対する累積操作
        k: 着目しているノード (1-indexed)
        l: 探索区間 st[l, r) の左端 (0-indexed)
        r: 探索区間 st[l, r) の右端 (0-indexed)
        """
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
        return self._query_topdown(a, b, k=1, l=0, r=len(self.st)//2)
        # return self._query_bottomup(a, b)


def solve_online(N, S, Q):
    tree = SegmentTree(N, op=or_, init_value=0)
    C = [ord(s) - ord("a") for s in S]
    for i in range(N):
        c = ord(S[i]) - ord("a")
        tree.update(i, 1 << c)

    for _ in range(Q):
        op, a, b = input().strip().split()
        if op == "1":
            i, c = int(a)-1, ord(b) - ord("a")
            tree.update(i, 1 << c)
        elif op == "2":
            l, r = int(a)-1, int(b)-1
            b = tree.query(l, r+1)
            s = 0
            while b > 0:
                if b & 1 == 1:
                    s += 1
                b >>= 1
            print(s)


if __name__ == '__main__':
    inputs = read()
    outputs = solve_online(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
