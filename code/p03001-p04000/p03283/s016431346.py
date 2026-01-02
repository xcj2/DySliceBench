from collections import Counter
from collections import deque
from functools import reduce
from pprint import pprint
import bisect
import copy
import fractions
import itertools
import math
import queue
import random
import sys
import time
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def MI(): return map(int, sys.stdin.readline().split())
def II(): return int(sys.stdin.readline())
def IS(): return input()
def C(x): return Counter(x)
def GCD_LIST(numbers): return reduce(fractions.gcd, numbers)
def LCM_LIST(numbers): return reduce(LCM, numbers)
def LCM(m, n): return (m * n // fractions.gcd(m, n))
class UnionFind():

    def __init__(self, n):
        self.n = n
        self.node = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def same(self, x, y):
        return bool(self.root(x) == self.root(y))

    def root(self, x):
        if self.node[x] == x:
            return x
        else:
            self.node[x] = self.root(self.node[x])  # 経路圧縮
            return self.node[x]

    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            return  # 結合不要
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.node[y] = x
        self.size[x] += self.size[y]

    def return_size(self, x):
        return self.size[self.root(x)]


n, m, q = MI()
train = [LI() for _ in range(m)]
query = [LI() for _ in range(q)]
table = [[0 for _ in range(n)] for _ in range(n)]
ruisekiwa = [[0 for _ in range(n)] for _ in range(n)]
# O(nm)
# for p, q in query:
#     cnt = 0
#     for left, right in train:
#         if p <= left and right <= q:
#             cnt += 1
#     print(cnt)
for left, right in train:
    table[left-1][right-1] += 1

# pprint(table, width=40)

for i in range(n):
    for j in range(n):
        ruisekiwa[i][j] = table[i][j]
        if i > 0:
            ruisekiwa[i][j] += ruisekiwa[i-1][j]
        if j > 0:
            ruisekiwa[i][j] += ruisekiwa[i][j-1]
        if i > 0 and j > 0:
            ruisekiwa[i][j] -= ruisekiwa[i-1][j-1]

# pprint(ruisekiwa, width=40)
for p, q in query:
    ans = ruisekiwa[q-1][q-1]
    if p-1 > 0:
        ans -= ruisekiwa[p-2][q-1]
        ans -= ruisekiwa[q-1][p-2]
        ans += ruisekiwa[p-2][p-2]
    print(ans)
