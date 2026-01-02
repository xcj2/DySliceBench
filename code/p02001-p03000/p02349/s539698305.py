
import sys
input = sys.stdin.readline

class Bit:
    def __init__(self, n):
        self.n = n
        self.tree = [0]*(n+1)
        self.el = [0]*(n+1)
        self.depth = n.bit_length()

    def sum(self, i):
        """ 区間[0,i) の総和を求める """
        s = 0
        i -= 1
        while i >= 0:
            s += self.tree[i]
            i = (i & (i + 1) )- 1
        return s

    def add(self, i, x):
        self.el[i] += x
        while i < self.n:
            self.tree[i] += x
            i |= i + 1

    def get(self, i, j=None):
        """ 部分区間和 [i, j) """
        if j is None:
            return self.el[i]
        if i == 0:
            return self.sum(j)
        return self.sum(j) - self.sum(i)

    def lower_bound(self, x, equal=False):
        """ (a0+a1+...+ai < x となる最大の i, その時の a0+a1+...+ai )
             a0+a1+...+ai <= x としたい場合は equal = True         """
        sum_ = 0
        pos = -1    # 1-indexed の時は pos = 0
        if not equal:
            for i in range(self.depth, -1, -1):
                k = pos + (1 << i)
                if k <= self.n and sum_ + self.tree[k] < x:
                    sum_ += self.tree[k]
                    pos += 1 << i
        if equal:
            for i in range(self.depth, -1, -1):
                k = pos + (1 << i)
                if k <= self.n and sum_ + self.tree[k] <= x:
                    sum_ += self.tree[k]
                    pos += 1 << i
        return pos, sum_

    def __getitem__(self, s):
        """ [a0, a1, a2, ...] """
        return self.el[s]

    def __iter__(self):
        """ [a0, a1, a2, ...] """
        for s in self.el[:self.n]:
            yield s

    def __str__(self):
        text1 = " ".join(["element: "] + list(map(str, self)))
        text2 = " ".join(["cumsum:  "] + list(str(self.sum(i)) for i in range(1, self.n + 1)))
        return "\n".join((text1, text2))


class BitImos:
    def __init__(self, n):
        self.n = n
        self.p = Bit(self.n + 1)
        self.q = Bit(self.n + 1)

    def add(self, s, t, x):
        """ 区間は閉区間 [s,t] で与えられる。原理は Imos法 と同じ。"""
        t += 1
        self.p.add(s, -x * s)
        self.p.add(t, x * t)
        self.q.add(s, x)
        self.q.add(t, -x)

    def sum(self, s, t):
        """ 半閉区間[s,t)の累積和を与える """
        return self.p.sum(t) + self.q.sum(t) * t - self.p.sum(s) - self.q.sum(s) * s

    def __getitem__(self, s):
        """ 区間加算後の s 番目の要素をO(log N)で取り出す。Imos法だとこの操作にO(N)かかる。"""
        return self.q.sum(s+1)

    def __iter__(self):
        """ max(self) で普段 Imos法 でやってることが出来る。"""
        for t in range(self.n):
            yield self.q.sum(t+1)

    def __str__(self):
        text1 = " ".join(["element: "] + list(map(str, self)))
        return text1

N, Q = map(int, input().split())
BI = BitImos(N)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 0:
        BI.add(q[1]-1,q[2]-1,q[3])
    else:
        print(BI[q[1]-1])


