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
        """
        (a0+a1+...+ai < x となる最大の i (存在しない時は -1 ) , その時の a0+a1+...+ai )
        a0+a1+...+ai <= x としたい場合は equal = True
        二分探索であるため、ai>=0 を満たす必要がある
        """
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

####################################################################################################

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
        return self.q.sum(s+1)      # sum は半開区間総和なので、s までの和を得るには s+1 としなければならない点に注意

    def __iter__(self):
        """ max(self) で普段 Imos法 でやってることが出来る。"""
        for t in range(self.n):
            yield self.q.sum(t+1)

    def __str__(self):
        text1 = " ".join(["element: "] + list(map(str, self)))
        return text1

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

    def bisect_left(self,x):
        if x <= self.n:
            return self.p.sum(x)
        else:
            return self.size

    def bisect_right(self,x):
        x += 1
        if x <= self.n:
            return self.p.sum(x)
        else:
            return self.size

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
        """
        元のリストをソートしたリストの k 番目の要素 (0-indexed)
        B[k] = sorted(A)[k]
        """
        if k >= 0:
            return self.minimum(k+1)
        else:
            return self.minimum(self.size + 1 + k)

    def __len__(self):
        return self.size

    def __iter__(self):
        for i in range(self.n+1):
            if self.p[i]:
                for _ in range(self.p[i]):
                    yield i

    def __str__(self):
        text1 = " ".join(list(map(str, self)))
        return "[" + text1 + "]"

####################################################################################################

class BitSet2:
    """ 座標圧縮が必要な場合 """
    def __init__(self, data, A=[]):
        """
        self.size: BitSetに含まれている要素の個数
        """
        """ BitSetに入り得る値を先読みした物を data に格納 """
        self.data = sorted(list(set(data)))
        self.n = len(self.data)
        self.p = Bit(self.n + 1)
        self.size = 0
        self.flip = 0
        self.code = {}
        self.decode = {}
        for i, b in enumerate(self.data):
            self.code[b] = i
            self.decode[i] = b
        for a in A:
            self.add(a)

    def add(self,x):
        self.p.add(self.code[x], 1)
        self.size += 1
        self.flip += self.size - self.p.sum(self.code[x]+1)        # 転倒数を使わないなら消してOK

    def remove(self,x):
        self.p.add(self.code[x], -1)
        self.size -= 1

    def order(self,x):
        """
        x が小さい順で何番目かを取得（1-indexed)
        BIT.order(x) = bisect_left(BIT.sort(),x) + 1
        BIT.minimum(BIT.order(x)) = BIT.lower_bound(x) = Aに含まれる x 以上の最小の要素
        """
        if x in self.code.keys():
            return self.p.sum(self.code[x]) + 1
        else:
            return self.p.sum(bisect_right(self.data, x)) + 1

    def bisect_left(self,x):
        if x in self.code.keys():
            return self.p.sum(self.code[x])
        else:
            return self.p.sum(bisect_right(self.data, x))

    def bisect_right(self,x):
        x += 1
        if x in self.code.keys():
            return self.p.sum(self.code[x])
        else:
            return self.p.sum(bisect_right(self.data, x))

    def count(self,x):
        return self.p[self.code[x]]

    def minimum(self,k=1):
        """ k 番目に小さい値を取得 """
        if k <= self.size:
            return self.decode[self.p.lower_bound(k)[0] + 1]
        else:
            sys.stderr.write("minimum: list index out of range (k={0})\n".format(k))

    def min(self):
        return self.minimum(1)

    def max(self):
        return self.decode[self.p.lower_bound(self.size)[0] + 1]

    def upper_bound(self,x):
        """ x以下の最大の要素の値を返す """
        if x in self.code.keys():
            y = self.code[x] + 1
        else:
            y = bisect_right(self.data, x)
        k = self.p.sum(y)
        if k:
            return self.minimum(k)
        else:
            sys.stderr.write("upper_bound: no element smaller than {0} in this BitSet\n".format(x))

    def lower_bound(self,x):
        """ x以上の最小の要素の値を返す """
        if x in self.code.keys():
            y = self.code[x]
        else:
            y = bisect_left(self.data, x)
        k = self.p.sum(y) + 1
        if k <= self.size:
            return self.minimum(k)
        else:
            sys.stderr.write("lower_bound: no element larger than {0} in this BitSet\n".format(x))

    def __getitem__(self, k):
        """
        元のリストをソートしたリストの k 番目の要素 (0-indexed)
        B[k] = sorted(A)[k]
        """
        if k >= 0:
            return self.minimum(k+1)
        else:
            return self.minimum(self.size + 1 + k)

    def __len__(self):
        return self.size

    def __iter__(self):
        for i in range(self.n+1):
            if self.p[i]:
                for _ in range(self.p[i]):
                    yield self.decode[i]

    def __str__(self):
        """ 配列をソートされた形で表示 """
        text1 = " ".join(list(map(str, self)))
        return "[" + text1 + "]"

#######################################################################

import sys
input = sys.stdin.readline
from bisect import bisect_left
from bisect import bisect_right
from heapq import *
N = int(input())
A = list(map(int, input().split()))
P = []
for a in A[:N]: heappush(P,a)
B = A[N:]
Q = BitSet2(B,B)
S2=sum(sorted(B)[:N])
S1=sum(A[:N])
res = S1-S2
for i in range(N):
    a = A[N+i]
    p = heappop(P)
    S1 += max(a - p, 0)
    heappush(P,max(a,p))
    q = Q[N-1]
    Q.remove(a)
    if a <= q:
        S2 += Q[N-1]-a
    res = max(S1-S2,res)
print(res)