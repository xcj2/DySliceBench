import sys
input = sys.stdin.readline
from bisect import bisect_left
from bisect import bisect_right


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

####################################################################################################


class BitSet:

    """ 挿入、削除、k番目の値を取得、全てがO(logN)で可能。重複にも対応。"""
    """ 原理的に ai>=0 であるため、二分探索が可能である点も重要　　　　　"""
    def __init__(self, n, A=[]):
        """
        :param n: Aの要素の最大値
        :param A:
        self.size: BitSetに含まれている要素の個数
        """
        self.n = n
        self.p = Bit(self.n + 1)
        self.size = 0
        self.flip = 0
        for a in A:
            self.add(a)

    def add(self,x):
        self.p.add(x, 1)
        self.size += 1
        self.flip += self.size - self.p.sum(x+1)        # 転倒数を使わないなら消してOK

    def remove(self,x):
        self.p.add(x, -1)
        self.size -= 1

    def order(self,x):
        """
        x が小さい順で何番目かを取得（1-indexed)
        BIT.order(x) = bisect_left(BIT.sort(),x) + 1
        BIT.minimum(BIT.order(x)) = BIT.lower_bound(x) = Aに含まれる x 以上の最小の要素
        """
        return self.p.sum(x) + 1

    def flip_counter(self):
        return self.flip

    def count(self,x):
        return self.p[x]

    def minimum(self,k=1):
        """ k 番目に小さい値を取得 （1-indexed）  """
        if k <= self.size:
            return self.p.lower_bound(k)[0] + 1
        else:
            sys.stderr.write("minimum: list index out of range (k={0})\n".format(k))

    def min(self):
        return self.minimum(1)

    def max(self):
        return self.p.lower_bound(self.size)[0] + 1

    def upper_bound(self,x):
        """ x以下の最大の要素の値を返す """
        k = self.p.sum(x+1)
        if k:
            return self.minimum(k)
        else:
            sys.stderr.write("upper_bound: no element smaller than {0} in this BitSet\n".format(x))

    def lower_bound(self,x):
        """ x以上の最小の要素の値を返す """
        k = self.p.sum(x) + 1
        if k <= self.size:
            return self.minimum(k)
        else:
            sys.stderr.write("lower_bound: no element larger than {0} in this BitSet\n".format(x))

    def __getitem__(self, k):
        """ ソートした時の k 番目の要素 (0-indexed)  """
        if k >= 0:
            return self.minimum(k+1)
        else:
            return self.minimum(self.size + 1 + k)

    def __iter__(self):
        for i in range(self.n+1):
            if self.p[i]:
                for _ in range(self.p[i]):
                    yield i

    def __str__(self):
        text1 = " ".join(list(map(str, self)))
        return "[" + text1 + "]"

####################################################################################################

def max2(x,y):
    return x if x > y else y

def min2(x,y):
    return x if x < y else y


N = int(input())
data = []
for i, p in enumerate(map(int, input().split())):
    data.append((i, p))
data.sort(key=lambda x:x[1])

i, p = data.pop()

BIT = BitSet(N)
BIT.add(i)
res = 0
while data:
    i, p = data.pop()
    x = BIT.order(i)
    R = BIT.minimum(x) if x <= BIT.size else N
    RR = BIT.minimum(x+1) if x+1 <= BIT.size else N
    L = BIT.minimum(x-1) if x-1 >= 1 else -1
    LL = BIT.minimum(x-2) if x-2 >= 1 else -1
    if i < R:
        res += p*(RR - R)*(i - L)
    if i > L:
        res += p*(L - LL)*(R - i)
    BIT.add(i)
print(res)