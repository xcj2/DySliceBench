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
table = [[0 for _ in range(n+1)] for _ in range(n+1)]
ruisekiwa = [[0 for _ in range(n+1)] for _ in range(n+1)]
for left, right in train:
    table[left][right] += 1
for i in range(1, n+1):
    for j in range(1, n+1):
        ruisekiwa[i][j] = table[i][j]
        if j > 1:
            ruisekiwa[i][j] += ruisekiwa[i][j-1]
        if i > 1:
            ruisekiwa[i][j] += ruisekiwa[i-1][j]
        if j > 1 and i > 1:
            ruisekiwa[i][j] -= ruisekiwa[i-1][j-1]
for p, q in query:
    print(ruisekiwa[q][q] - ruisekiwa[p-1][q] - ruisekiwa[q][p-1] + ruisekiwa[p-1][p-1])


