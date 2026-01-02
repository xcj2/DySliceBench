import math
from operator import itemgetter as ig
from collections import defaultdict as dd
# 定数
INF = float("inf")
MOD = int(1e9 + 7)
# データ構造：ヒープ
import heapq
class heapque:
    def __init__(self, *args):
        self.que = []
        for arg in args:
            self.push(arg)
    def push(self, v):
        heapq.heappush(self.que, v)
    def pop(self):
        return heapq.heappop(self.que)
# 最大公約数 / 最小公倍数
def gcd(v1, v2):
    if v2 == 0:
        return v1
    return gcd(v2, v1 % v2)
def lcm(v1, v2):
    return (v1 // gcd(v1, v2)) * v2
# 二分探索
def bsr(a, v, lo=0, hi=None):
    if hi == None:
        hi = len(a) - 1
    if hi < lo:
        return lo
    mi = (lo + hi) // 2
    if v < a[mi]:
        return bsr(a, v, lo, mi - 1)
    else:
        return bsr(a, v, mi + 1, hi)
# Union-Find木
class uft:
    def __init__(self, n):
        self.height = [1] * n
        self.group = [-1] * n
    def root(self, v):
        if self.group[v] < 0:
            return v
        self.group[v] = self.root(self.group[v])
        return self.group[v]
    def size(self, v):
        return - self.group[self.root(v)]
    def merge(self, v1, v2):
        v1, v2 = self.root(v1), self.root(v2)
        if v1 == v2:
            return
        if self.height[v1] < self.height[v2]:
            self.group[v2] += self.group[v1]
            self.group[v1] = v2
            self.height[v2] = max(self.height[v1] + 1, self.height[v2])
        else:
            self.group[v1] += self.group[v2]
            self.group[v2] = v1
            self.height[v1] = max(self.height[v1] , self.height[v2] + 1)

def main():
    L, R = map(int, input().split())
    if 2019 < (R - L + 1):
        print(0)
    else:
        min_mod = INF
        for l in range(L, R + 1):
            for r in range(l + 1, R + 1):
                min_mod = min(min_mod, l * r % 2019)
        print(min_mod)

main()
