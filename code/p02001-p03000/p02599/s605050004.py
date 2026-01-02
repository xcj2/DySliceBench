import sys
from operator import itemgetter
def input(): return sys.stdin.readline().rstrip()

class BinaryIndexedTree:  # 0-index !!!
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)  # 内部的には1-indexで扱う

    def add(self, i, x):  # 0-index
        i += 1  # 内部的には1-indexで扱う
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def sum(self, i):  # 0-index  sum of [0,i)
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def query(self, l, r):  # 0-index  sum of [l,r)
        return self.sum(r) - self.sum(l)

# ---------------------- #

n, q = (int(x) for x in input().split())
C = list(int(x) - 1 for x in input().split())
LR = [tuple(int(x) for x in input().split()) for _ in range(q)]

bit = BinaryIndexedTree(n)
color_right_index = [-1] * n
queries = [(i, l - 1, r - 1) for i, (l, r) in enumerate(LR)]
queries.sort(key=itemgetter(2))
ANS = [0] * q
k = 0
for i, l, r in queries:
    while k <= r and k <= n:
        color = C[k]
        if color_right_index[color] != -1:
            bit.add(color_right_index[color], -1)
        color_right_index[C[k]] = k
        bit.add(k, 1)
        k += 1
    ANS[i] = bit.query(l, r + 1)

for ans in ANS:
    print(ans)
