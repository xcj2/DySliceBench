import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
class UnionFind(object):
    def __init__(self, n = 1):
        self.link = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.link[x] == x:
            return x

        # re-connect union find to make the height of tree lower
        # you can use while, but recursion makes it easier to reconnect
        self.link[x] = self.find(self.link[x])
        return self.link[x]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.size[x] < self.size[y]:
            x, y = y, x
        self.link[y] = x
        self.size[x] += self.size[y]
    
    def get_size(self, x):
        x = self.find(x)
        return self.size[x]

N, M = map(int, input().split())
u = UnionFind(N)

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    u.unite(a, b)

d = defaultdict(int)
for i in range(N):
    x = u.find(i)
    d[x] += 1
print(max(d.values()))