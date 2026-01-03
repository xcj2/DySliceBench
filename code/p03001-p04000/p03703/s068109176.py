class Bit:
    def __init__(self, n):
        self.n = n
        self.tree = [0]*(n+1)
        self.el = [0]*(n+1)
        self.depth = n.bit_length() - 1

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

class BitSet2:
    """ 座標圧縮が必要な場合 """
    def __init__(self, data, A=[]):
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
        self.flip += self.size - self.p.sum(self.code[x]+1)

    def remove(self,x):
        self.p.add(x, -1)
        self.size -= 1

    def flip_counter(self):
        return self.flip



####################################################################################################

import sys
input = sys.stdin.readline
from itertools import accumulate
N, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))
S = [0] + list(accumulate(A))
T = []
for i, s in enumerate(S):
    T.append(s-K*i)
B = BitSet2(T,T)
print(N*(N+1)//2-B.flip_counter())