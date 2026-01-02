import sys
input = sys.stdin.readline

class Bit:
    def __init__(self, n):
        self.n = n
        self.tree = [0]*(n+1)
        self.elem = [0] * (n + 1)
        self.depth = n.bit_length() - 1

    def sum(self, i):
        """ 区間[0,i) の総和を求める """
        s = 0
        i -= 1
        while i >= 0:
            s += self.tree[i]
            i = (i & (i + 1) )- 1
        return s

    def built(self, array):
        """ array を初期値とするBITを構築 """
        for i, a in enumerate(array):
            self.add(i, a)

    def add(self, i, x):
        """ i 番目の要素に x を足す """
        self.elem[i] += x
        while i < self.n:
            self.tree[i] += x
            i |= i + 1

    def get(self, i, j=None):
        """ 部分区間和 [i, j) """
        if j is None:
            return self.elem[i]
        if i == 0:
            return self.sum(j)
        return self.sum(j) - self.sum(i)

    def lower_bound(self, x, equal=False):
        """ (a0+a1+...+ai < x となる最大の i, その時の a0+a1+...+ai )
             a0+a1+...+ai <= x としたい場合は equal = True
             二分探索であるため、ai>=0 を満たす必要がある"""
        sum_ = 0
        pos = -1    # 1-indexed の時は pos = 0
        if not equal:
            for i in range(self.depth, -1, -1):
                k = pos + (1 << i)
                if k < self.n and sum_ + self.tree[k] < x:  # 1-indexed の時は k <= self.n
                    sum_ += self.tree[k]
                    pos += 1 << i
        if equal:
            for i in range(self.depth, -1, -1):
                k = pos + (1 << i)
                if k < self.n and sum_ + self.tree[k] <= x: # 1-indexed の時は k <= self.n
                    sum_ += self.tree[k]
                    pos += 1 << i
        return pos, sum_

    def __getitem__(self, s):
        """ [a0, a1, a2, ...] """
        return self.elem[s]

    def __iter__(self):
        """ [a0, a1, a2, ...] """
        for s in self.elem[:self.n]:
            yield s

    def __str__(self):
        text1 = " ".join(["element:            "] + list(map(str, self)))
        text2 = " ".join(["cumsum(1-indexed):  "] + list(str(self.sum(i)) for i in range(1, self.n + 1)))
        return "\n".join((text1, text2))

class RangeSet:
    """ 与えられた数列の区間内の種類数を求める """
    def __init__(self, n, array, query):
        """
        :param n: 要素数
        :param array: 整数で種類付けされた数列
        """
        self.n = n
        self.BIT = Bit(self.n)
        self.lastAppeared = [-1]*(self.n + 1)
        self.array = []
        self.query = []
        for i, c in enumerate(array):
            self.array.append(c)
            self.lastAppeared[c] = i
        for i, lr in enumerate(query):
            l, r = lr
            l -= 1
            r -= 1
            self.query.append((l,r,i))
        self.query.sort(key=lambda x: x[1])
        for x in self.lastAppeared:
            if x != -1:
                self.BIT.add(x, 1)

    def solve(self):
        res = [0] * len(self.query)
        r0 = 0
        for l, r, i in self.query:
            for R in range(r0, r + 1):
                self.BIT.add(self.lastAppeared[self.array[R]], -1)
                self.lastAppeared[self.array[R]] = R
                self.BIT.add(self.lastAppeared[self.array[R]], 1)
            res[i] = self.BIT.get(l, r + 1)
            r0 = r
        return res

##############################################################################################

N, Q = map(int, input().split())
C = list(map(int, input().split()))
query = []
for i in range(Q):
    l, r = map(int, input().split())
    query.append((l,r))

RS = RangeSet(N, C, query)
res = RS.solve()
print(*res, sep="\n")
