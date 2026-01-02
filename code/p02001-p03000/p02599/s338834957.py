import sys
input = sys.stdin.readline

class Bit:
    def __init__(self, n):
        """
        :param n: 最大の要素数
        """
        self.n = n
        self.tree = [0]*(n+1)
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
        while i < self.n:
            self.tree[i] += x
            i |= i + 1

    def get(self, i, j):
        """ 部分区間和 [i, j) """
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

    def __getitem__(self, i):
        """ [a0, a1, a2, ...] """
        return self.get(i, i+1)

    def __iter__(self):
        """ [a0, a1, a2, ...] """
        for i in range(self.n):
            yield self.get(i, i+1)

    def __str__(self):
        text1 = " ".join(["element:            "] + list(map(str, self)))
        text2 = " ".join(["cumsum(1-indexed):  "] + list(str(self.sum(i)) for i in range(1, self.n + 1)))
        return "\n".join((text1, text2))

class ListList:
    """ tupleを一番目の添え字に関してソートする"""
    def __init__(self, max_value_list):
        """
        :param max_value_list: tuple = (i, j, k) を考えた時、  max_value_list = (j_max, k_max)
        """
        self.list_list = []
        self.separation = [0]
        self.max_value_list = list(map(lambda x: x.bit_length(), max_value_list))
        for a in self.max_value_list:
            self.separation.append(self.separation[-1] + a)
        self.separation.reverse()
        self.mask = list(map(lambda x: x-1, self.separation))

    def append(self, array):
        temp = 0
        for x, i in zip(array, self.separation):
            temp += x<<i
        self.list_list.append(temp)

    def sort(self, reverse=False):
        return self.list_list.sort(reverse=reverse)

    def __getitem__(self, item):
        temp = self.list_list[item]
        array = []
        for a in self.max_value_list:
            array = [temp&((1<<a)-1)] + array
            temp>>=a
        array = [temp] + array
        return array

    def __iter__(self):
        for i in range(len(self.list_list)):
            yield self[i]

    def __str__(self):
        text = []
        for a in self:
            text.append("[" + ", ".join(list(map(str, a))) + "]")
        return "[" + ", ".join(text) + "]"

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
        self.Q = len(query)
        self.query = ListList((len(array),self.Q))
        for i, c in enumerate(array):
            self.array.append(c)
            self.lastAppeared[c] = i
        for i, lr in enumerate(query):
            l, r = lr
            l -= 1
            r -= 1
            self.query.append((r,l,i))
        self.query.sort()
        for x in self.lastAppeared:
            if x != -1:
                self.BIT.add(x, 1)

    def solve(self):
        res = [0] * self.Q
        r0 = 0
        for r, l, i in self.query:
            for R in range(r0, r + 1):
                self.BIT.add(self.lastAppeared[self.array[R]], -1)
                self.lastAppeared[self.array[R]] = R
                self.BIT.add(R, 1)
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


