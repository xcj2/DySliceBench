# -*- coding: utf-8 -*-
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**6)

class UnionFind:
    """素集合を木構造として管理する。"""
    def __init__(self, n):
        self.parent = [-1] * n
        self.n = n
        self.cnt = n
 
    def root(self, x):
        """要素xの代表元を求める。O(α(N))"""
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]
 
    def merge(self, x, y):
        """要素xを含む集合と要素yを含む集合を併合する。O(α(N))"""
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        self.cnt -= 1
        return True
 
    def is_same(self, x, y):
        """要素x, yが同じ集合に属するかどうかを求める。O(α(N))"""
        return self.root(x) == self.root(y)
 
    def size(self, x):
        """要素xを含む集合の要素数を求める。O(α(N))"""
        return -self.parent[self.root(x)]
 
    def count(self):
        """集合の個数を求める。O(1)"""
        return self.cnt
 
    def groups(self):
        """集合を列挙する。list[list[int]]で返す。O(N)"""
        res = [[] for _ in range(self.n)]
        for i in range(self.n):
            res[self.root(i)].append(i)
        return [group for group in res if group]

N,Q = map(int,readline().split())
uf = UnionFind(N)

for _ in range(Q):
    x,y = map(int,readline().split())
    x-=1; y-=1
    uf.merge(x,y)

print(uf.count()-1)