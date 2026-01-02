import math, heapq
from operator import itemgetter as ig
from collections import defaultdict as dd
# 定数
INF = float("inf")
MOD = int(1e9 + 7)
# ヒープ
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
# グラフ
class graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
    def append(self, v1, v2, cost=1):
        self.graph[v1].append((v2, cost))
    # 最短経路：ダイクストラ法(Dijkstra's Algorithm)
    def dks(self, v):
        costs = [INF] * self.n
        costs[v] = 0
        done = [False] * self.n
        heap = heapque((0, v))
        while heap.que:
            c_cost, c_index = heap.pop()
            if done[c_index]:
                continue
            done[c_index] = True
            for n_index, n_cost in self.graph[c_index]:
                if c_cost + n_cost < costs[n_index]:
                    costs[n_index] = c_cost + n_cost
                    heap.push((costs[n_index], n_index))
        return costs

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    ab = sorted(AB)
    heap = heapque()
    v, i = 0, 0
    for m in range(1, M + 1):
        while i < N:
            if ab[i][0] <= m:
                heap.push(-ab[i][1])
                i += 1
            else:
                break
        if heap.que:
            v += -heap.pop()
    print(v)

main()
